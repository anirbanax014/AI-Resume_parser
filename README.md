🤖 AI Resume Parser
This project is an intelligent resume parser that uses the Google Gemini API to instantly extract and structure key information from PDF resumes. Upload a file to parse contact info, skills, and work experience into a clean, organized format. The application is built with a Python Flask backend and a modern, responsive frontend.
✨ Key Features
AI-Powered Parsing: Leverages the gemini-1.5-flash model for high-accuracy data extraction.

Structured JSON Output: Organizes parsed data into categories like name, contact, skills, and employment history.

PDF Processing: Extracts text directly from PDF documents using PyPDF.

Responsive UI: A clean user interface built with TailwindCSS for a seamless experience on any device.

Secure Backend: Ensures safe file handling and API key management.

🛠️ Tech Stack
Backend: Python, Flask, Google Generative AI library, PyPDF

Frontend: HTML, CSS, TailwindCSS, JavaScript

API: Google Gemini API

⚙️ How It Works
A user uploads a PDF through the web interface. The Flask server receives the file, extracts its text content using PyPDF, and sends the text to the Google Gemini API for analysis. The API returns structured JSON data, which is then rendered back to the user on the frontend.

🚀 Getting Started
Prerequisites: Python 3.8+ and a Google Gemini API Key.

Clone the repository and navigate into it:

Bash

git clone https://github.com/your-username/ai-resume-parser.git
cd ai-resume-parser
Create and activate a virtual environment:

Bash

# For macOS/Linux: python3 -m venv venv && source venv/bin/activate
# For Windows: python -m venv venv && .\venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
Set up your environment:
Create a .env file in the root directory and add your API key:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
Run the application:

Bash

flask run --port=8000
Access the parser at http://127.0.0.1:8000.

🔐 Security
Security is handled through PDF-only file validation, secure API key management using .env files, protected file storage, and robust error handling for invalid inputs.
