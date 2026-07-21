import os
import requests
from PIL import Image
from io import BytesIO
from gtts import gTTS

def generate_image(prompt):

    prompt = prompt.replace(" ", "%20")

    url = f"https://image.pollinations.ai/prompt/{prompt}"

    response = requests.get(url, timeout=120)

    image = Image.open(BytesIO(response.content))

    os.makedirs("images", exist_ok=True)

    image_path = "images/story_scene.png"

    image.save(image_path)

    return image_path

def generate_audio(text):

    os.makedirs("audio", exist_ok=True)

    audio_path = "audio/story.mp3"

    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    tts.save(audio_path)

    return audio_path