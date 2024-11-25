import streamlit as st
import openai
from dotenv import load_dotenv
import os
from get_prompts import prompts
from chatbot import create_response_streamlit


# Load the API key from the .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Ensure the API key is set
if not api_key:
    st.error("API key is missing. Please check your .env file.")
    st.stop()

# Set up the OpenAI API key directly
openai.api_key = api_key

# List of predefined system prompts
keys_to_include = ["MAS", "NAI", "OTI", "OTE", "OAI", "OAE", "NTI", "NTE", "NAE", "Custom Social"]
system_prompts = {key: prompts[key] for key in keys_to_include if key in prompts}


# Streamlit page setup
st.title("AI Chatbot")

# Sidebar for settings and document upload
with st.sidebar:
    st.header("Settings")
    engine = st.selectbox("Choose the AI model:", ["gpt-4", "gpt-4o", "gpt-4o-mini"], index=2)
    temperature = st.slider("Select the temperature:", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    st.write(f"Current settings: Model = {engine}, Temperature = {temperature}")

    # st.header("Upload a Document")
    # uploaded_file = st.file_uploader("Choose a file", type=['txt', 'pdf', 'docx'])
    # if uploaded_file is not None:
    #     st.write("Uploaded File:", uploaded_file.name)

    st.header("System Prompt")
    selected_system_prompt = st.selectbox("Choose a system prompt:", list(system_prompts.keys()))
    # Show and allow editing of the selected system prompt
    system_prompt_text = st.text_area("Edit the system prompt:", value=system_prompts[selected_system_prompt], height=100)
    st.write(system_prompt_text)
    

# Main area for chat
st.write("Enter your prompt and get a response from the AI.")
user_prompt = st.text_input("Enter your prompt:", placeholder="Type something here...")

# Button to generate response
if st.button("Generate Response"):
    if user_prompt:
        with st.spinner('AI is generating a response...'):
            response = create_response_streamlit(system_prompt_text, user_prompt, engine, temperature)
            st.write(response)
    else:
        st.error("Please enter a prompt.")
