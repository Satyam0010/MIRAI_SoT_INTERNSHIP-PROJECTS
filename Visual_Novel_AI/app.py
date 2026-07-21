import os
import json

import streamlit as st
from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT

from utils import generate_image, generate_audio


load_dotenv()

@st.cache_resource
def get_client():
    return genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

st.set_page_config(
    page_title="AI Visual Novel",
    page_icon="📖",
    layout="wide"
)


client = get_client()

def generate_scene(user_input):

    response = st.session_state.chat.send_message(user_input)

    data = json.loads(response.text)

    # Image generation
    try:
        image_path = generate_image(data["image_prompt"])
        data["image"] = image_path

    except Exception:
        data["image"] = None
        st.toast("🖼️ Image server is busy. Skipping visual...")

    # Audio generation
    try:
        audio_path = generate_audio(data["story_text"])
        data["audio"] = audio_path

    except Exception:
        data["audio"] = None
        st.toast("🔊 Audio generation failed.")

    st.session_state.scene = data

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model="gemini-2.5-flash",
        config={
            "system_instruction": SYSTEM_PROMPT,
            "response_mime_type": "application/json"
        }
    )

if "history" not in st.session_state:
    st.session_state.history = []

if "scene" not in st.session_state:
    st.session_state.scene = None


st.title("📖 Multi-Modal Visual Novel")

st.sidebar.title("🎬 Story Settings")


genre = st.sidebar.selectbox(
    "Genre",
    [
        "Fantasy",
        "Sci-Fi",
        "Horror",
        "Mystery",
        "Adventure"
    ]
)

art_style = st.sidebar.selectbox(
    "Art Style",
    [
        "Anime",
        "Pixar",
        "Realistic",
        "Watercolor",
        "Oil Painting"
    ]
)

st.write("### Current Settings")

st.write(f"Genre : **{genre}**")

st.write(f"Art Style : **{art_style}**")

if st.button("🚀 Start Story"):

    generate_scene(
        f"""
Genre: {genre}

Art Style: {art_style}

Start a brand new story.
"""
    )

if st.session_state.scene:
    if st.session_state.scene["image"]:
        st.image(
          st.session_state.scene["image"],
         use_container_width=True
        )

    if st.session_state.scene["audio"]:
        st.audio(
            st.session_state.scene["audio"]
        )
    st.subheader("📖 Story")
    st.write(st.session_state.scene["story_text"])

    st.subheader("🎨 Scene")

    st.subheader("Choose your next move")

    for option in st.session_state.scene["options"]:

        if st.button(option):

            generate_scene(option)

            st.rerun()