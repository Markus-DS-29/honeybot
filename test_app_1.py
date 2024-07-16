import streamlit as st
import requests
from bs4 import BeautifulSoup

# Title of the app
st.title("Simple Streamlit App with BeautifulSoup")

# Input box
user_input = st.text_input("Enter a URL:")

# Fetch and display the title of the webpage
if user_input:
    try:
        # Fetch the content from the URL
        response = requests.get(user_input)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get the title of the webpage
        title = soup.title.string if soup.title else 'No title found'
        
        # Display the title
        st.write(f'Title of the webpage: {title}')
    except requests.RequestException as e:
        st.write(f'Error fetching the URL: {e}')
