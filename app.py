import streamlit as st
from PIL import Image
from prompt_helper import generate_prompt

st.set_page_config(page_title="AI Prompt Engineering Assistant", layout="centered")
st.title("🧠 AI Prompt Engineering Assistant")

uploaded_images = st.file_uploader("Upload Moodboard Images", type=["jpg", "png"], accept_multiple_files=True)
style = st.text_input("Style (e.g., cinematic, minimal)")
subject = st.text_input("Subject (e.g., a farmer using AI)")
mood = st.text_input("Mood (e.g., peaceful, futuristic)")
camera_info = st.text_input("Camera & Lighting Details (optional)")

if st.button("Generate Prompt"):
    images = [Image.open(img) for img in uploaded_images]
    prompt = generate_prompt(style, subject, mood, camera_info)
    st.text_area("🎯 Generated Prompt", prompt, height=300)
    st.download_button("Download Prompt", prompt, file_name="structured_prompt.txt")
