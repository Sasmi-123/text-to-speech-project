import streamlit as st
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
import torch
import soundfile as sf

# Load models
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

# Random speaker embedding
speaker_embeddings = torch.randn(1, 512)

st.title("Text-to-Speech")

text = st.text_area("Enter text to convert to speech")

if st.button("Generate Speech"):
    if text.strip() != "":
        inputs = processor(text=text, return_tensors="pt")
        speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

        sf.write("speech.wav", speech.numpy(), samplerate=16000)

        st.audio("speech.wav")
        st.markdown('<a href="speech.wav">Download audio</a>', unsafe_allow_html=True)
    else:
        st.warning("Please enter text")





