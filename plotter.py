
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('datasets/98183f57-358c-4915-80f7-1e74e7a439e3.csv')

# Create the histogram
fig = px.histogram(df, x='wt', nbins=10)

# Display the plot
st.plotly_chart(fig)

