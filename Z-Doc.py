import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.title("Z-Doc")

if st.button("Book an appointment"):
    st.write("Or call us at 080-23458021")

name = st.text_input("Name:")
st.write(name)

address = st.text_area("Enter your address:")
st.write(address)

symptoms_check = st.text_area("Please enter symptoms, if any:")
st.write(symptoms_check)

st.date_input("Enter a date:")

st.time_input("Enter a time:")

st.slider("Age",min_value = 7,max_value=90,value = 30,step = 2)

uploaded_files = st.file_uploader("Upload your recent check-up slip", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    







