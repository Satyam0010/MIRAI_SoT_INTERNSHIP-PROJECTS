import os
import random
import time


import streamlit as st
from dotenv import load_dotenv
from google import genai

from personalities import PERSONALITIES
from prompts import SYSTEM_PROMPT
from styles import CUSTOM_CSS



load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.set_page_config(
    page_title="AI Multiverse 2.0",
    page_icon="🌌",
    layout="wide"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)



if "favorite" not in st.session_state:
    st.session_state.favorite = {}


st.title("🌌 AI MULTIVERSE 2.0")

st.caption(
    "Talk with heroes, scientists, athletes and legendary personalities."
)



st.sidebar.title("⚙ AI Settings")

category = st.sidebar.selectbox(
    "Category",
    list(PERSONALITIES.keys())
)

search = st.sidebar.text_input(
    "🔍 Search Personality"
)

names = list(PERSONALITIES[category].keys())

if search:

    names = [
        p for p in names
        if search.lower() in p.lower()
    ]

if len(names) == 0:

    st.sidebar.warning("No personality found.")

    st.stop()

personality = st.sidebar.selectbox(
    "Choose Personality",
    names
)

reply_style = st.sidebar.selectbox(
    "Response Style",
    [
        "Friendly",
        "Funny",
        "Professional",
        "Motivational",
        "Sarcastic",
        "Teacher"
    ]
)

reply_length = st.sidebar.selectbox(
    "Response Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

creativity = st.sidebar.slider(
    "Creativity",
    0,
    100,
    70
)

surprise = [
    "Tell me a joke.",
    "Motivate me.",
    "Teach me AI.",
    "Explain Quantum Physics.",
    "Give me startup ideas.",
    "Write a poem.",
    "Teach me DSA.",
    "How can I become successful?"
]

if st.sidebar.button("🎲 Surprise Me"):
    st.info(f"Suggestion: {random.choice(surprise)}")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()

st.subheader("💬 Chat")


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if message := st.chat_input("Say something..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    with st.chat_message("user"):
        st.markdown(message)


    personality_prompt = PERSONALITIES[category][personality]

    style_prompt = {
        "Friendly": "Be warm and friendly.",
        "Funny": "Be humorous and entertaining.",
        "Professional": "Answer professionally.",
        "Motivational": "Motivate the user.",
        "Sarcastic": "Use light sarcasm where appropriate.",
        "Teacher": "Explain everything clearly like a teacher."
    }

    length_prompt = {
        "Short": "Maximum 60 words.",
        "Medium": "Around 120 words.",
        "Long": "Around 250 words."
    }

    history = ""

    for chat in st.session_state.messages[-6:]:
        history += f"{chat['role']}: {chat['content']}\n"

    prompt = f"""

    {SYSTEM_PROMPT}

    PERSONALITY

    {personality_prompt}

    STYLE

    {style_prompt[reply_style]}

    LENGTH

    {length_prompt[reply_length]}

    CREATIVITY LEVEL

    {creativity}/100

    PREVIOUS CONVERSATION

    {history}

    CURRENT USER MESSAGE

    {message}

    Remember:

    Stay completely in character.

    Never reveal you are an AI.

    Never break character.

    """

    start = time.time()

    with st.spinner("🌌 Entering the Multiverse..."):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            reply = response.text

            with st.chat_message("assistant"):
                st.markdown(reply)

        except Exception as e:

            st.error(e)

            st.stop()

    end = time.time()

    st.session_state.messages.append(
        {
        "role": "assistant",
        "content": reply
        }
    )

