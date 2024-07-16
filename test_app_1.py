import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input box
user_input = st.text_input("Enter something:")

# Display the input back to the user
if user_input:
    st.write(f'You entered: {user_input}')