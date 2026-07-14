import streamlit as st
from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


st.set_page_config(
    page_title="Memory Vault Chatbot",
    page_icon="🧠"
)

st.title("🧠 Memory Vault Chatbot")
st.caption("Powered by Gemini")



personality = st.sidebar.selectbox(
    "Choose Personality",
    [
        "Friendly",
        "Professional",
        "Teacher",
        "Motivational",
        "Funny"
    ]
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()



if "messages" not in st.session_state:
    st.session_state.messages = []



if len(st.session_state.messages) == 0:
    st.info("👋 Hello! I'm your Memory Vault Chatbot. I can remember our conversation during this session.")



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("Say something..."):

 
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    full_prompt = f"""
You are a {personality} AI Assistant.

Respond according to this personality.

User:
{prompt}
"""

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=full_prompt
            )

            reply = response.text

            st.markdown(reply)

    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )



st.sidebar.markdown("---")

st.sidebar.write(f"Total Messages : {len(st.session_state.messages)}")

user_count = len(
    [m for m in st.session_state.messages if m["role"] == "user"]
)

bot_count = len(
    [m for m in st.session_state.messages if m["role"] == "assistant"]
)

st.sidebar.write(f"User Messages : {user_count}")
st.sidebar.write(f"AI Messages : {bot_count}")



chat = ""

for msg in st.session_state.messages:
    chat += f"{msg['role'].upper()} : {msg['content']}\n\n"

st.sidebar.download_button(
    "📥 Download Chat",
    chat,
    file_name="chat_history.txt"
)