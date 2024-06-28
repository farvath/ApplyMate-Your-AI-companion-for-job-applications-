import streamlit as st
import requests

st.title('Rasa Chatbot Demo')

user_input = st.text_input('Enter your message:')
submit_button = st.button('Send')

if submit_button and user_input:
    try:
        # Send user message to Rasa server
        rasa_url = "http://localhost:5056/webhook"
        response = requests.post(rasa_url, json={'sender': 'user', 'message': user_input})
        
        print(response)  # Print the response for debugging
        
        # Handle response
        if response.status_code == 200:
            bot_responses = response.json()
            if bot_responses is not None:
                for bot_response in bot_responses:
                    st.text(f"Bot: {bot_response['text']}")
            else:
                st.error("Empty response from Rasa server.")
        else:
            st.error(f"Failed to get response from Rasa. Status code: {response.status_code}")
    
    except requests.exceptions.ConnectionError as e:
        st.error(f"Connection error: {e}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request error: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
