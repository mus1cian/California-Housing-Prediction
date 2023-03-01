import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title("California Housing House Value Prediction")
st.markdown("Random Forest Training to determine median house value based on several features")

col1, col2 = st.columns(2)
with col1:
    longitude = st.number_input("Longitude", max_value=0)
    age = st.number_input("Housing Median Age", min_value=0)
    total_bedrooms = st.number_input("Total bedrooms", min_value=1)
    households = st.number_input("Households", min_value=1)
with col2:
    latitude = st.number_input("Latitude")
    total_rooms = st.number_input("Total rooms", min_value=1)
    population = st.number_input("Population")
    income = st.number_input("Median income")

ocean_proximity = st.selectbox("Ocean Proximity: ",
                     ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])


m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #F63366;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #ffffff;
    color:#000000;
    font:"sans serif";
    }
</style>""", unsafe_allow_html=True)

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
    st.balloons()

