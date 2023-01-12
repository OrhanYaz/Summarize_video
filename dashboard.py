import requests
import streamlit as st

# Set the API endpoint
API_ENDPOINT = "http://your_api_endpoint"

def get_api_output(text):
    # Send a POST request to the API with the user's text as the data
    response = requests.post(API_ENDPOINT, data={'text': text})
    
    # Return the API's response
    return response.text

def main():
    st.title("Text Input Example")
    text = st.text_input("Enter some text:")
    if st.button("Submit"):
        st.success("The API returned: {}".format(get_api_output(text)))
