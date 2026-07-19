import streamlit as st
import requests
import random
from urllib.parse import quote
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="AI Image Studio",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 AI Image Studio")

st.write(
    "Generate beautiful AI images using Pollinations AI."
)


st.sidebar.header("⚙️ Settings")



art_style = st.sidebar.selectbox(
    "Choose Art Style",
    [
        "Realistic",
        "Anime",
        "Fantasy",
        "Cyberpunk",
        "Oil Painting",
        "Watercolor",
        "Pixel Art"
    ]
)

width = st.sidebar.slider(
    "Image Width",
    min_value=256,
    max_value=1024,
    value=512,
    step=64
)

height = st.sidebar.slider(
    "Image Height",
    min_value=256,
    max_value=1024,
    value=512,
    step=64
)


magic_enhance = st.sidebar.checkbox(
    "✨ Enable Magic Enhance"
)


user_prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: A futuristic city at sunset"
)

col1, col2 = st.columns(2)

generate = col1.button("🎨 Generate Image")

surprise = col2.button("🎲 Surprise Me")


surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A dragon flying over New York City",
    "A giant turtle carrying an entire village",
    "A futuristic underwater kingdom with glowing whales"
]


def generate_image(prompt):

    full_prompt = f"{prompt}, {art_style}"

    if magic_enhance:
        full_prompt += (
            ", masterpiece, 8k resolution, highly detailed, "
            "trending on artstation, unreal engine 5 render"
        )

    encoded_prompt = quote(full_prompt)

    url = (
    f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    f"?width={width}&height={height}"
)

    with st.spinner("Generating image..."):


        response = requests.get(url, timeout=60)
        if response.status_code == 200:


            img = Image.open(BytesIO(response.content))
            st.image(
                response.content,
                caption="Generated Image",
                use_container_width=True
            )

            st.download_button(
                "📥 Download Image",
                data=response.content,
                file_name=f"{art_style}_image.png",
                mime="image/png"
            )

        else:
            st.error("Image generation failed. Please try again.")


if generate:

    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:
        generate_image(user_prompt)


if surprise:

    random_prompt = random.choice(surprise_prompts)

    st.success(f"🎲 Surprise Prompt:\n\n{random_prompt}")

    generate_image(random_prompt)


