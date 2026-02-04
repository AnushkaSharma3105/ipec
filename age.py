import streamlit as st 

st.title("Age and City")

age = st.slider("Enter you age: ", 1, 100)
city = st.selectbox("Select your city: ", ['Delhi', 'Mumbai', 'Bangalore', 'Pune'])

if st.button("Your Details:"):
    st.write("Your age is: ", age)
    st.write("You live in: ", city)