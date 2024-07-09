from dotenv import load_dotenv
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

load_dotenv()  # take environment variables from .env.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="ImageInsight - Image analyser")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');
    body {
        background-color: #000000;
        font-family: 'Oswald';
    }
    .main {
        color: #ffffff;
        background-color: #000000;
        border-radius: 10px;
        padding: 20px;
    }
    .stTextInput > div > div > input {
        border: 2px solid #ccc;
        border-radius: 5px;
        padding: 15px;
        font-size: 24px;
        color: #000000; /* Black color for input text */
        width: 100%;
        font-family: 'Oswald';
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        font-family: 'Roboto', sans-serif;
    }
    .stButton > button:hover {
        background-color: #ffffff;
        color: #4CAF50;
    }
    .stHeader {
        color: #ffffff !important;
        font-weight: bold !important;
        font-style: italic;
        font-size: 36px !important;
        font-family: 'Roboto', sans-serif !important;
    }
    .input-label {
        color: #ffffff;
        font-weight: bold;
        font-style: italic;
        font-size: 30px;
        font-family: 'Roboto', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="stHeader">Hey there! I would love to help you with analysis of your image!🐥</h1>', unsafe_allow_html=True)

input_text = st.text_input("Input Prompt:", key="input", help="Enter your prompt here")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# If ask button is clicked
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader("The Response is")
    st.write(response)
