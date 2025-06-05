from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np
import json

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()
    
    # Create company-model mapping for the JavaScript
    company_models = {}
    for company in companies:
        company_models[company] = sorted(car[car['company'] == company]['name'].unique())
    
    return render_template('index.html', 
                         companies=companies, 
                         car_models=car_models, 
                         years=year,
                         fuel_types=fuel_type,
                         company_models=company_models)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Extract data from JSON
        company = data.get('company')
        car_model = data.get('car_model')  # Changed from 'car_models'
        year = data.get('year')
        fuel_type = data.get('fuel_type')
        kms_driven = data.get('kms_driven')  # Changed from 'driven'
        
        # Validate required fields
        if not all([company, car_model, year, fuel_type, kms_driven]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Convert to appropriate types
        try:
            year = int(year)
            kms_driven = int(kms_driven)
        except ValueError:
            return jsonify({'error': 'Invalid numeric values'}), 400
        
        # Create prediction dataframe
        prediction_data = pd.DataFrame({
            'name': [car_model],
            'company': [company],
            'year': [year],
            'kms_driven': [kms_driven],
            'fuel_type': [fuel_type]
        })
        
        # Make prediction
        prediction = model.predict(prediction_data)
        predicted_price = np.round(prediction[0], 2)
        
        print(f"Prediction: {predicted_price}")
        
        return jsonify({'predicted_price': predicted_price})
        
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)