# main.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    st.set_page_config(page_title="F1nalyze", page_icon="🏎️", layout="wide")
    st.title("🏎️ F1nalyze: F1 Driver Standings Prediction")
    page = st.sidebar.radio("Navigate", ["Project Overview", "Data Insights", "Model Performance", "About"])

    if page == "Project Overview":
        show_project_overview()
    elif page == "Data Insights":
        show_data_insights()
    elif page == "Model Performance":
        show_model_performance()
    else:
        show_about()

def show_project_overview():
    st.header("📄 Project Overview")
    st.markdown("""
    - Predict F1 driver finishing positions  
    - Part of Kaggle F1nalyze Datathon  
    - Ranked **23rd out of 50** teams  
    - Best RMSE: **3.469**
    """)

def show_data_insights():
    st.header("📊 Data Insights")
    st.markdown("### Processing Steps")
    st.markdown("- Data Cleaning\n- Feature Engineering\n- Feature Selection")

    st.markdown("### Distribution of Grid Positions")
    pos = list(range(1, 21))
    freq = [np.random.randint(100, 1000) for _ in pos]
    fig = px.bar(x=pos, y=freq, labels={'x': 'Grid Position', 'y': 'Frequency'})
    st.plotly_chart(fig)

def show_model_performance():
    st.header("📈 Model Performance")
    models = ['Decision Tree', 'Random Forest', 'Logistic Regression']
    rmse = [5.72, 4.51, 3.46]
    fig = px.bar(x=models, y=rmse, title='Model RMSE Comparison')
    st.plotly_chart(fig)

def show_about():
    st.header("ℹ️ About")
    st.markdown("""
    - Created by **Team Frostbiters**  
    - Hosted on [GitHub](https://github.com/RonitJariwala/f1nalyze)  
    - Inspired by Kaggle F1nalyze Datathon
    """)

if __name__ == "__main__":
    main()
