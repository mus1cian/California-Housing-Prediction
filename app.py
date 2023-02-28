import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title("Predicting median house value")
st.markdown("Model to determine the median house value based on the income of the person")

col1, col2 = st.columns(2)
with col1:
    longitude = st.number_input("Longitude")
    age = st.number_input("Housing Median Age")
    total_bedrooms = st.number_input("Total bedrooms")
    households = st.number_input("Households")
with col2:
    latitude = st.number_input("Latitude")
    total_rooms = st.number_input("Total rooms")
    population = st.number_input("Population")
    income = st.number_input("Median income")

ocean_proximity = st.selectbox("Ocean Proximity: ",
                     ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])


if st.button("Predict house value"):  
    ocean = 0 if ocean_proximity == '<1H OCEAN' else 1 if ocean_proximity == 'INLAND' else 2 if ocean_proximity == 'ISLAND' else 3 if ocean_proximity == 'NEAR BAY' else 4 
    data = pd.DataFrame({
            'longitude': [longitude],
            'latitude': [latitude],
            'housing_median_age': [age],
            'total_rooms': [total_rooms],
            'total_bedrooms': [total_bedrooms],
            'population': [population],
            'households': [households],
            'median_income': [income],
            'ocean_proximity': [ocean_proximity]
        }) 
    result = predict(data)
    st.text(result[0]) 
