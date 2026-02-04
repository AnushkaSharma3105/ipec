import streamlit as st 

st.title("basic calculator app")

num1 = st.number_input("Enter first number: ")
num2 = st.number_input("Enter second number: ")

operation = st.selectbox("Select operations: ", ['+', '-', '*', '/'])

if st.button("calculate"):
    if operation == '+':
        st.write(num1+num2)
    elif operation == '-':
        st.write(num1-num2)
    elif operation == '*':
        st.write(num1*num2)
    elif operation == '/':
        if num2 != 0:
            st.write(num1/num2)
        else:
            st.error("Division by zero is now allowed")

