
import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
df = pd.read_csv('datasets/323bc711-ff94-47b2-9640-ee1ed3fbca54.csv')

# Create the plot
fig = px.scatter(df, x='wt', y='cyl', title='Weight vs Cylinder')

# Display the plot using Streamlit
st.plotly_chart(fig)

