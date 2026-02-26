**🎙 AI Text-to-Speech Web Application using SpeechT5**

This project is an AI-powered Text-to-Speech (TTS) web application built using Microsoft’s pre-trained SpeechT5 model and deployed with Streamlit.

The application converts user-provided text into natural-sounding speech using deep learning techniques.

**🚀 Features**

🔹 Convert text into natural AI-generated speech

🔹 Uses Microsoft SpeechT5 pre-trained model

🔹 Interactive and user-friendly Streamlit interface

🔹 Real-time speech audio generation

🔹 Downloadable speech output (.wav file)

**🛠 Tech Stack**

Python

Hugging Face Transformers

SpeechT5 Model

PyTorch

Streamlit

SoundFile

**🧠 How It Works****

User enters text in the Streamlit interface

Text is processed using Hugging Face SpeechT5 Processor

SpeechT5 model generates speech waveform

Output audio is saved as a .wav file

Audio is played inside the web application

**📂 Project Structure**
text-to-speech-project/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Required dependencies
├── speech.wav          # Generated speech output
├── README.md           # Project documentation
└── .gitignore
⚙ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/text-to-speech-project.git
cd text-to-speech-project
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
streamlit run app.py

The application will open in your browser.

**📸 Output Screenshot**



Example:

![App Screenshot](screenshot.png)
🎯 Future Improvements

Add multiple voice support

Deploy application online (Streamlit Cloud)

Add language selection feature

Improve speech naturalness

🙌 Learning Outcome

This project helped me understand:

Integration of pre-trained deep learning models

Hugging Face Transformers workflow

Building AI-powered web applications

Deploying ML models using Streamlit
