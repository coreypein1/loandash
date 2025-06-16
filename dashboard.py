import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv('results/results_df.csv')

results_df = load_data()

st.title("Model Performance Dashboard")
st.write("This dashboard provides an overview of model performance metrics.")

col1, col2, col3 = st.columns(3)

st.subheader("Model Performance Table")
st.dataframe(results_df.style.format({
    "accuracy": "{:.2f}",
    "mae": "{:.2f}",
    "rmse": "{:.2f}",
    "C": "{:.2f}"
}))

with col1:
    st.subheader('Accuracy Progression')
    fig_acc = px.line(
        results_df,
        x='C',
        y='accuracy',
        color='max_iter',
        title='Model Accuracy vs C Parameter',
        labels={'C': 'C Parameter', 'accuracy': 'Accuracy'},
        markers=True
    )
    st.plotly_chart(fig_acc)

with col2:
    st.subheader('MAE Progression')
    fig_mae = px.line(
        results_df,
        x='C',
        y='mae',
        color='max_iter',
        title='Model MAE vs C Parameter',
        labels={'C': 'C Parameter', 'mae': 'Mean Absolute Error'},
        markers=True
    )
    st.plotly_chart(fig_mae)
    
with col3:
    st.subheader('RMSE Progression')
    fig_rmse = px.line(
        results_df,
        x='C',
        y='rmse',
        color='max_iter',
        title='Model RMSE vs C Parameter',
        labels={'C': 'C Parameter', 'rmse': 'Root Mean Squared Error'},
        markers=True
    )
    st.plotly_chart(fig_rmse)