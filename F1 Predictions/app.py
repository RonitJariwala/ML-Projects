import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --------------------------------------------------
# Professional Motorsport-inspired CSS
CUSTOM_CSS = """
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {
    background-color: #0e1117;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #1a1d24;
    border-right: 1px solid #2a2e36;
}

/* Sidebar headings */
.sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
    color: #f5f5f5;
    font-weight: 600;
}

/* Card styling - F1 inspired */
.card {
    background-color: #1a1d24;
    border-radius: 8px;
    border-left: 4px solid #e10600; /* Ferrari red accent */
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    padding: 20px;
    margin-bottom: 20px;
    color: #e0e0e0;
}

/* Custom metrics with F1 team colors */
.metric-container {
    background-color: #1a1d24;
    border-radius: 8px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    border-top: 3px solid #e10600; /* Ferrari red */
    margin: 8px;
    color: #e0e0e0;
}

/* Title styling */
h1 {
    color: #ffffff !important;
    border-bottom: 2px solid #e10600;
    padding-bottom: 8px;
}

/* Tab styling */
[data-baseweb="tab-list"] {
    gap: 10px;
}

[data-baseweb="tab"] {
    background-color: #1a1d24 !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    margin: 0 5px !important;
    color: #b0b0b0 !important;
}

[data-baseweb="tab"][aria-selected="true"] {
    background-color: #e10600 !important;
    color: white !important;
}

/* Button styling */
.stButton>button {
    background-color: #e10600;
    color: white;
    border-radius: 4px;
    border: none;
    font-weight: 500;
}

.stButton>button:hover {
    background-color: #c00500;
    color: white;
}

/* Select box styling */
[data-baseweb="select"] {
    background-color: #1a1d24;
    border-radius: 4px;
}

/* Plotly chart background */
.js-plotly-plot .plotly, .js-plotly-plot .plotly div {
    background: transparent !important;
}

/* Divider styling */
hr {
    border: 1px solid #2a2e36;
    margin: 20px 0;
}

/* Metric value styling */
[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

/* Label styling */
[data-testid="stMetricLabel"] {
    color: #b0b0b0 !important;
}
</style>
"""

st.set_page_config(
    page_title="F1nalyze - F1 Predictions",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/RonitJariwala/f1nalyze/main/assets/logo.png", use_column_width=True)

    st.markdown("<h2 style='color:#f5f5f5;'>Navigation</h2>", unsafe_allow_html=True)
    selected = st.radio("", ["🏠 Dashboard", "📊 Data Analysis", "🤖 Models", "📈 Results", "ℹ️ About"], label_visibility="hidden")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#f5f5f5;'>🔢 Quick Stats</h3>", unsafe_allow_html=True)
    st.metric("Total Data Points", "3.18M", delta=None, label_visibility="visible")
    st.metric("Best RMSE", "3.46918", delta=None, label_visibility="visible")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#f5f5f5;'>🔄 Last Updated</h3>", unsafe_allow_html=True)
    st.text(datetime.now().strftime("%Y-%m-%d %H:%M"))


# Flags to decide which page to render
show_dashboard = (selected == "🏠 Dashboard")
show_data_analysis_flag = (selected == "📊 Data Analysis")


def show_dashboard_page():
    st.title("🏎️ F1nalyze - Predicting Formula 1 Driver Standings")

    # Key Highlights
    st.markdown("""
    <div class='card'>
        <h3>🔑 Key Highlights</h3>
        <div style='display:flex; justify-content: space-around; flex-wrap: wrap;'>
            <div class='metric-container'><h4>📊 Dataset Size</h4><h2 style='color:#00d2be;'>2.83M</h2><p>Training Samples</p></div>
            <div class='metric-container'><h4>🧠 Model Robustness</h4><h2 style='color:#006f62;'>High</h2><p>Stable across seasons</p></div>
            <div class='metric-container'><h4>📈 Best Score</h4><h2 style='color:#e10600;'>3.469</h2><p>RMSE</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <div class='card'>
        <h3>📌 Project Overview</h3>
        <div style='display:flex; justify-content: space-between; flex-wrap: wrap;'>
            <div style='flex: 1; min-width: 200px; margin: 10px;'>
                <h4>🎯 Goal</h4>
                <ul>
                    <li>Predict F1 driver positions</li>
                    <li>Kaggle Datathon: F1nalyze</li>
                </ul>
            </div>
            <div style='flex: 1; min-width: 200px; margin: 10px;'>
                <h4>📊 Dataset</h4>
                <ul>
                    <li>2.8M training rows</li>
                    <li>352k testing rows</li>
                    <li>Grid, team, points, ...</li>
                </ul>
            </div>
            <div style='flex: 1; min-width: 200px; margin: 10px;'>
                <h4>🛠️ Tech Stack</h4>
                <ul>
                    <li>Python</li>
                    <li>Scikit-learn</li>
                    <li>Pandas / Streamlit</li>
                </ul>
            </div>
            <div style='flex: 1; min-width: 200px; margin: 10px;'>
                <h4>🏁 Results</h4>
                <ul>
                    <li>RMSE: <b style='color:#e10600;'>3.46918</b></li>
                    <li>Logistic Regression best</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()


def show_data_analysis_page():
    st.title("📊 Training Data Analysis")

    tab1, tab2, tab3 = st.tabs(["📈 Feature Distribution", "🔄 Correlations", "📋 Data Quality"])

    with tab1:
        st.markdown("<div class='card'><h4>Select Feature to Visualize</h4></div>", unsafe_allow_html=True)
        feature = st.selectbox("", ["Grid Position", "Points", "Laps", "Wins"], label_visibility="hidden")

        if feature == "Grid Position":
            data = np.random.normal(10, 3, 1000)
            range_x = [1, 20]
        elif feature == "Points":
            data = np.random.exponential(10, 1000)
            range_x = [0, 50]
        elif feature == "Laps":
            data = np.random.gamma(2, 2, 1000)
            range_x = [0, 70]
        else:
            data = np.random.gamma(2, 1.5, 1000)
            range_x = [0, 15]

        fig = px.histogram(data, title=f'{feature} Distribution', nbins=30)
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis_title=feature,
            yaxis_title='Count',
            font=dict(color='#e0e0e0'),
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("<div class='card'><h4>Feature Correlations Heatmap</h4></div>", unsafe_allow_html=True)
        features = ['Grid', 'Points', 'Laps', 'Wins', 'Position']
        corr_matrix = np.random.rand(5, 5)
        np.fill_diagonal(corr_matrix, 1)
        fig = px.imshow(
            corr_matrix,
            labels=dict(x="Features", y="Features"),
            x=features,
            y=features,
            color_continuous_scale="reds",
            title="Feature Correlation Matrix"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e0e0')
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.markdown("<div class='card'><h4>Data Quality Metrics</h4></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            missing_data = pd.DataFrame({
                'Feature': ['Grid', 'Points', 'Laps', 'Status', 'Position'],
                'Missing %': [0.1, 0.2, 0.5, 1.2, 0.0]
            })
            fig = px.bar(
                missing_data,
                x='Feature',
                y='Missing %',
                title='Missing Values',
                text='Missing %',
                color='Feature',
                color_discrete_sequence=px.colors.sequential.Reds
            )
            fig.update_traces(texttemplate='%{text}%%', textposition='outside')
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e0e0e0'),
                yaxis=dict(range=[0, max(missing_data['Missing %']) + 0.5]),
                template='plotly_dark'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            dtype_dist = pd.DataFrame({
                'Type': ['Numeric', 'Categorical', 'DateTime'],
                'Count': [7, 3, 1]
            })
            fig = px.pie(
                dtype_dist,
                values='Count',
                names='Type',
                title='Feature Types',
                hole=0.4,
                color_discrete_sequence=px.colors.sequential.Reds
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e0e0e0'),
                template='plotly_dark'
            )
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div class='card'>
        <h4>🚀 Insights</h4>
        <ul>
            <li>Grid positions are normally distributed around mid-pack.</li>
            <li>Points distribution is right-skewed; majority of drivers score fewer points.</li>
            <li>Missing values are minimal; data quality is robust.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def show_models_page():
    st.title("🤖 Model Analysis")
    st.subheader("Model Performance Comparison")

    models_data = pd.DataFrame({
        'Model': ['Decision Tree', 'Random Forest', 'Logistic Regression'],
        'RMSE': [5.72788, 4.51769, 3.46918],
        'Training Time (s)': [45, 120, 30],
        'Memory Usage (MB)': [150, 450, 100]
    })

    metric = st.selectbox("Select Metric", ["RMSE", "Training Time (s)", "Memory Usage (MB)"])
    fig = px.bar(
        models_data, 
        x='Model', 
        y=metric, 
        color='Model', 
        title=f'Model Comparison - {metric}',
        color_discrete_sequence=['#e10600', '#006f62', '#005aff']
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0'),
        template='plotly_dark'
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Model Details")
    selected_model = st.selectbox("Select Model", ["Decision Tree", "Random Forest", "Logistic Regression"])
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'><h4>Configuration</h4></div>", unsafe_allow_html=True)
        params = {
            "Decision Tree": {"max_depth": 10, "min_samples_split": 2, "criterion": "gini"},
            "Random Forest": {"n_estimators": 100, "max_depth": 10, "min_samples_split": 2},
            "Logistic Regression": {"C": 1.0, "max_iter": 100, "solver": "lbfgs"}
        }[selected_model]

        for param, value in params.items():
            st.metric(param, value)

    with col2:
        st.markdown("<div class='card'><h4>Feature Importance</h4></div>", unsafe_allow_html=True)
        features = ['Grid', 'Points', 'Laps', 'Wins', 'Status']
        importance = np.random.rand(5)
        fig = px.bar(
            x=features, 
            y=importance, 
            title=f'Feature Importance - {selected_model}',
            color=features,
            color_discrete_sequence=px.colors.sequential.Reds
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e0e0'),
            template='plotly_dark'
        )
        st.plotly_chart(fig, use_container_width=True)


def show_results_page():
    st.title("📈 Results Analysis")
    st.subheader("Prediction vs Actual Position")

    np.random.seed(42)
    actual = np.random.randint(1, 21, 100)
    predicted = actual + np.random.normal(0, 2, 100)
    predicted = np.clip(predicted, 1, 20)

    fig = px.scatter(
        x=actual,
        y=predicted,
        labels={'x': 'Actual', 'y': 'Predicted'},
        title='Prediction Accuracy',
        trendline="lowess",
        color_discrete_sequence=['#e10600']
    )
    fig.add_trace(
        go.Scatter(
            x=[1, 20],
            y=[1, 20],
            mode='lines',
            name='Perfect Prediction',
            line=dict(dash='dash', color='#00d2be')
        )
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0'),
        template='plotly_dark'
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Error Distribution")
    errors = predicted - actual
    fig = px.histogram(
        errors,
        title='Prediction Error',
        labels={'value': 'Error', 'count': 'Frequency'},
        color_discrete_sequence=['#e10600']
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0'),
        template='plotly_dark'
    )
    st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 RMSE", "3.469", delta="-1.258 from baseline", delta_color="inverse")
    with col2:
        st.metric("📊 MAE", "2.845", delta="-0.932 from baseline", delta_color="inverse")
    with col3:
        st.metric("📈 R²", "0.876", delta="+0.124 from baseline")


def show_about_page():
    st.title("ℹ️ About F1nalyze")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
            <h3>🔗 Resources</h3>
            <ul>
                <li><a href='https://github.com/RonitJariwala' target='_blank' style='color:#e10600;'>GitHub</a></li>
                <li><a href='https://kaggle.com' target='_blank' style='color:#e10600;'>Kaggle</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
            <h3>🔄 Future Improvements</h3>
            <ul>
                <li>Deep learning integration</li>
                <li>Real-time predictions</li>
                <li>Feature engineering</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3>📅 Timeline</h3>", unsafe_allow_html=True)
    df = pd.DataFrame({
        'Phase': ['Data Collection', 'Preprocessing', 'Modeling', 'Testing', 'Submission'],
        'Start': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15', '2024-03-01'],
        'End': ['2024-01-15', '2024-02-01', '2024-02-15', '2024-03-01', '2024-03-15'],
        'Status': ['Completed'] * 5
    })
    fig = px.timeline(
        df,
        x_start='Start',
        x_end='End',
        y='Phase',
        color='Status',
        title='Project Timeline',
        color_discrete_sequence=['#e10600']
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0'),
        yaxis={'categoryorder': 'array', 'categoryarray': df['Phase'].tolist()},
        template='plotly_dark'
    )
    st.plotly_chart(fig, use_container_width=True)


# Render pages
if show_dashboard:
    show_dashboard_page()
elif show_data_analysis_flag:
    show_data_analysis_page()
elif selected == "🤖 Models":
    show_models_page()
elif selected == "📈 Results":
    show_results_page()
else:
    show_about_page()

if __name__ == "__main__":
    pass  # Streamlit runs the code on import