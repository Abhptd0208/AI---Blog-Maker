import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

genai.configure(api_key=google_gemini_api_key)

# Configure API key
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Load the model
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Generate a comprehensive, engaging blog post relevant to the given title \"Effects of Generative Al\" and keywords \"Artificial Creativity, Ethical Implications, Technology Innovation, Machine Learning Applications, Al Impact on Society\". Make sure to incorporate these keywords in the blog post. The blog should be approximately 500 words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout. **Title: Effects of Generative Al: Shaping the Future of Creativity, Innovation, and Society**",
)

# Set up Streamlit layout
st.set_page_config(layout='wide')
st.title('✍️ BlogMaker : Your 🤖 AI Writing Companion')
st.subheader("Now you can draft perfect blogs with the help of AI-Blogcraft is your new AI Blog companion")

# Sidebar for user input
with st.sidebar:
    st.title('Enter details for the blog you want to generate')
    
    # Input fields
    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma-separated)")
    num_words = st.slider("Number of Words", min_value=200, max_value=1000, step=200)
    num_images = st.number_input("Number of Images", min_value=0, max_value=5, step=1)
    
    submit_button = st.button('Generate Blog')

# Chat session setup
chat_session = model.start_chat()

# Generate blog on button click
if submit_button:
    if blog_title and keywords:
        prompt = f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."
        response = chat_session.send_message(prompt)
        st.write(response.text)
    else:
        st.error("Please fill in the blog title and keywords.")
