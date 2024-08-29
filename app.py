import streamlit as st

st.title("My First Streamlit App")

# Add a text input
name = st.text_input("Enter your name:")

# Add a checkbox
if st.checkbox("Click here"):
  st.write("You clicked the checkbox!")

# Add a slider
age = st.slider("Select your age", 0, 100)

# Add a button
if st.button("Click me"):
  st.write(f"Hello, {name}! You are {age} years old.")
