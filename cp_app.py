import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

# Load the model
model = pk.load(open('C:/Users/missj/Desktop/CPP/pipeline.pkl', 'rb'))

st.header('Car Price Prediction ML Model')

# Load the dataset
cars_data = pd.read_csv('C:/Users/missj/Desktop/CPP/new car.csv')

# User inputs
brand_name = st.selectbox('Select Car Brand', cars_data['brand_name'].unique())
year = st.slider('Car Manufactured Year', 1994, 2024)
km_driven = st.slider('No of Kms Driven', 11, 200000)
fuel = st.selectbox('Fuel Type', cars_data['fuel'].unique())
seller_type = st.selectbox('Seller Type', cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission Type', cars_data['transmission'].unique())
owner = st.selectbox('Owner Type', cars_data['owner'].unique())
mileage = st.slider('Car Mileage (kmpl)', int(cars_data['mileage'].min()), int(cars_data['mileage'].max()))
engine = st.slider('Engine CC', int(cars_data['engine'].min()), int(cars_data['engine'].max()))
max_power = st.slider('Max Power (bhp)', int(cars_data['max_power'].min()), int(cars_data['max_power'].max()))
seats = st.slider('Number of Seats', int(cars_data['seats'].min()), 5)

# Prediction button
if st.button("Predict"):
    # Preprocessing input data
    input_data = pd.DataFrame(
        [[brand_name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=['brand_name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
    )

    # Predict the price
    car_price = model.predict(input_data)
    st.success(f"Predicted Car Price: ₹{car_price[0]:,.2f}")