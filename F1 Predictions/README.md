# F1nalyze - Predicting Formula 1 Driver Standings with Machine Learning🚀

### Dataset Description

We were provided with three CSV files:
- `train.csv`: Training data used to train the models.
- `test.csv`: Testing data for which we had to predict and submit the output with minimum RMSE.
- `validation.csv`: Validation data used to validate our model's prediction and try to reduce RMSE.

Download Dataset From This Link:
https://www.kaggle.com/competitions/f1nalyze-datathon-ieeecsmuj/data

## Data Preprocessing

1. **Handling Missing Data**: 
   - Checked for missing values and occurrences of `\N` in both the train and test datasets.
   - Dropped columns in the training dataset with more than 100 occurrences of `\N`.
   - Filled missing values in the 'status' and 'result_driver_standing' columns with the mode.

2. **Label Encoding**:
   - Used `LabelEncoder` to convert categorical features such as `positionText_x`, `nationality`, `company`, and `status` into numerical values.

3. **Feature Selection**:
   - Selected a specific set of columns based on their relevance for both the train and test datasets.

## Model Training

We experimented with three different machine learning models to predict driver standings:

1. **Decision Tree Classifier**:
   - Initial model used to predict the standings.
   - RMSE on validation data: **5.72788**.

2. **Random Forest Classifier**:
   - Improved model using an ensemble method to enhance prediction accuracy.
   - RMSE on validation data: **4.51769**.

3. **Logistic Regression**:
   - Applied logistic regression for classification after standardizing the data.
   - RMSE on validation data: **3.46918**.

## Model Evaluation

We used Root Mean Squared Error (RMSE) to evaluate the model's performance on the validation dataset. RMSE was calculated for each model:

- **Decision Tree RMSE**: 3.46918
- **Random Forest RMSE**: 3.46918
- **Logistic Regression RMSE**: 3.46918

## Submission

Predictions were made on the test dataset using all three models, and the results were saved in CSV files for submission:

- `dt_predictions.csv`: Decision Tree predictions.
- `rf_predictions.csv`: Random Forest predictions.
- `lr_predictions.csv`: Logistic Regression predictions.


## Learnings and Insights

This project provided valuable experience in:

- **Data Preprocessing**: Handling missing data, label encoding, and feature selection.
- **Model Evaluation**: Using RMSE as a key metric for model performance.
- **Machine Learning**: Implementing and comparing different machine learning algorithms for classification.

Despite not winning, the F1nalyze project was a significant learning opportunity, allowing us to enhance our skills in data science and machine learning within the dynamic context of Formula 1 racing.

## Conclusion

The F1nalyze project showcased the potential of machine learning in predicting complex outcomes in sports analytics. We look forward to further refining our models and exploring additional features and techniques to improve prediction accuracy in future endeavors.

