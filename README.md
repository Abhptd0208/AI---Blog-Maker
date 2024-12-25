✍️ BlogMaker: Your 🤖 AI Writing Companion

**BlogMaker** is a web-based application that helps you generate high-quality blog posts using the power of AI. With BlogMaker, you can easily create comprehensive, engaging, and original blog posts tailored to your needs.

**Features**
- 🌟 **AI-Powered Blog Creation**: Generate blog posts based on your input title and keywords.
- 🎯 **Customizable Output**: Specify the number of words and images to suit your blog requirements.
- 🧠 **Smart Keyword Integration**: Automatically incorporate your provided keywords into the blog post.
- 💡 **Simple Interface**: User-friendly design powered by Streamlit for easy interaction.


  **Tech Stack**
- **Frontend**: [Streamlit](https://streamlit.io/) for the user interface.
- **AI Model**: [Google Generative AI (Gemini 1.5)](https://developers.generativeai.google).
- **Backend**: Python for API integration.

 **Setup and Usage**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blogmaker.git
   cd blogmaker
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your API key:
   - Create a file named `apikey.py`.
   - Add the following line with your API key:
     ```python
     google_gemini_api_key = "your_google_gemini_api_key"
     ```
4. Run the app:
   ```bash
   streamlit run App.py
   ```
5. Open the app in your browser at `http://localhost:8501`.

