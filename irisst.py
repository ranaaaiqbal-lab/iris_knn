import streamlit as st
import pickle
st.write("Hello ,let's register first")
sepallength=st.number_input("Enter your sepal length")
sepalwidth=st.number_input("Enter your sepal width")
petallength=st.number_input("Enter your petal length")
petalwidth=st.number_input("Enter your petal width")
if st.button("Click me"):
    with open(r"C:\Users\BAPS\Desktop\internship\iris_model.pkl", "rb") as file:
        loaded_model = pickle.load(file)
    result=loaded_model.predict([[sepallength,sepalwidth,petallength,petalwidth]])
    st.write(result)