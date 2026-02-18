import streamlit as st
import pandas as pd

st.title('🚕 Pick up Trip')
st.info('welcome to our taxi driver app based on machine learning')

model = joblib.load("model.pkl")

distance = st.number_input("Distance")
passengers = st.number_input("Passengers")

if st.button("Predict"):
    X = np.array([[distance, passengers]])
    pred = model.predict(X)
    st.write("Price:", pred[0])

