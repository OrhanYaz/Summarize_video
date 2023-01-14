import os
from urllib.parse import quote

import requests
import streamlit as st

# Set the API endpoint
API_ENDPOINT = "http://127.0.0.1:5000/get_summary/"


def get_api_output(text):
    
    # Url to api
    text = quote(text)
    video_url = os.path.join(API_ENDPOINT,text) 
    
    # Send a POST request to the API with the user's text as the data
    response = requests.get(video_url).json()
    
    # Return the API's response
    return response['summary']

def main():
    st.title("Youtube Summary")
    text = st.text_input("Enter youtube url:")
    if st.button("Submit"):
        st.success("Here is your summary: {}".format(get_api_output(text)))


if __name__ == '__main__':
    main()
