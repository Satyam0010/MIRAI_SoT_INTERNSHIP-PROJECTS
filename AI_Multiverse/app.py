import os
import random
import time
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from google import genai

from personalities import PERSONALITIES
from prompts import SYSTEM_PROMPT
from styles import CUSTOM_CSS
from utils import count_words, count_characters, format_chat

# -----------------------------
# CONFIG
# -----------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.set_page_config(
    page_title="AI Multiverse 2.0",
    page_icon="🌌",
    layout="wide"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "message" not in st.session_state:
    st.session_state.message = ""

if "favorite" not in st.session_state:
    st.session_state.favorite = {}

# -----------------------------
# HEADER
# -----------------------------

st.title("🌌 AI MULTIVERSE 2.0")

st.caption(
    "Talk with heroes, scientists, athletes and legendary personalities."
)

# -----------------------------
# SIDEBAR
# -----------------------------

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

    st.session_state.message = random.choice(surprise)

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.history = []

    st.rerun()

# -----------------------------
# CHAT INPUT
# -----------------------------

st.subheader("💬 Chat")

message = st.text_area(
    "Enter your message",
    value=st.session_state.message,
    height=150,
    placeholder="Ask anything..."
)

st.caption(
    f"Characters : {len(message)}"
)

send = st.button(
    "🚀 Send",
    use_container_width=True
)


# -----------------------------
# GENERATE RESPONSE
# -----------------------------

if send:

    if message.strip() == "":
        st.warning("Please enter a message.")
        st.stop()

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

    # Previous conversation memory
    history = ""

    for chat in st.session_state.history[-6:]:

        history += f"""
User:
{chat['user']}

Assistant:
{chat['ai']}
"""

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

        except Exception as e:

            st.error(e)

            st.stop()

    end = time.time()

    st.session_state.history.append(

        {
            "user": message,
            "ai": reply,
            "personality": personality,
            "time": datetime.now().strftime("%I:%M %p"),
            "response_time": round(end - start, 2)
        }

    )

    st.session_state.message = ""

    # -----------------------------
# CHAT HISTORY
# -----------------------------

st.divider()

for chat in st.session_state.history:

    st.markdown(f"""
<div class='chat-user'>

👤 <b>You</b><br><br>

{chat['user']}

</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class='chat-ai'>

<b>{chat['personality']}</b>

<br>

🕒 {chat['time']}

<br><br>

{chat['ai']}

</div>
""", unsafe_allow_html=True)