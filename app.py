import streamlit as st

# Set the title of the app
st.title("Simple Calculator")

# Create input fields for the numbers
num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

# Create radio buttons for the operations
operation = st.radio("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on the operation selected
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!"
    
    st.write("Result:", result)

