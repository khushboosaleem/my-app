import joblib
import pandas as pd
import streamlit as st

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction")

st.write("Enter house details to predict the price.")

area = st.slider("Area (sq ft)", 500, 5000, 1500)

bedrooms = st.selectbox(
    "Bedrooms",
    [1, 2, 3, 4, 5, 6]
)

bathrooms = st.selectbox(
    "Bathrooms",
    [1, 2, 3, 4, 5, 6]
)

location = st.selectbox(
    "Location",
    ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Faisalabad"]
)

house_age = st.slider(
    "House Age",
    0, 30, 5
)

if st.button("Predict Price"):

    new_house = pd.DataFrame({
        "area_sqft": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "location": [location],
        "house_age": [house_age]
    })

    price = model.predict(new_house)[0]

    st.success(f"Estimated House Price: Rs. {price:,.0f}")





