import streamlit as st
import pandas as pd

df = pd.read_csv('/workspaces/loandash/data/DLDCS.csv')

st.title('Loan Dashboard')
st.write('Corey Pein')

st.dataframe(df, height=200)

st.bar_chart(df['interest_rate'])