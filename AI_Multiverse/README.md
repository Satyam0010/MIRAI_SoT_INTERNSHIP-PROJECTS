# 🌌 AI Multiverse 2.0

An interactive AI-powered chatbot built with **Streamlit** and **Google Gemini**, where users can converse with a wide variety of famous personalities from different universes, professions, and backgrounds.

Whether it's **Iron Man**, **Batman**, **Sherlock Holmes**, **Albert Einstein**, **Elon Musk**, or a **Ronaldo Fan**, the chatbot responds while staying true to the selected personality using carefully designed prompts.

---

## ✨ Features

* 🎭 Multiple AI personalities across different categories
* 🔍 Search personalities instantly
* 📂 Category-wise personality selection
* 🧠 Context-aware conversations with chat memory
* 🎨 Multiple response styles
* 📏 Adjustable response length
* 🎲 Surprise prompt generator
* 💬 Beautiful chat interface
* 📊 Chat statistics
* 🗑️ Clear conversation
* ⚡ Powered by Google Gemini 2.5 Flash
* 🌙 Modern Streamlit-based user interface

---

## 🧩 Personality Categories

* 🦸 Marvel
* 🦇 DC
* ⚽ Sports
* 🧠 Scientists
* 🚀 Entrepreneurs
* 🎬 Entertainment

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini API**
* **python-dotenv**
* **HTML & CSS (Custom Styling)**

---

## 📁 Project Structure

```text
AI_Multiverse_2/
│
├── app.py
├── personalities.py
├── prompts.py
├── styles.py
├── utils.py
├── requirements.txt
├── .env
├── .gitignore
└── assets/
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI_Multiverse_2
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Select a personality category.
2. Choose your favorite personality.
3. Customize the response style and length.
4. Enter your question.
5. Gemini generates a response while staying in character.
6. Previous conversation history is used to provide more contextual and engaging responses.

---

## 🎯 Learning Outcomes

This project demonstrates:

* Prompt Engineering
* AI-powered conversational interfaces
* Google Gemini API integration
* Streamlit application development
* Session state management
* Modular Python project architecture
* UI customization using HTML and CSS
* Environment variable management

---

## 🔮 Future Enhancements

* Voice interaction
* Conversation export (PDF)
* User-created personalities
* Persistent chat history
* Theme customization
* Multi-personality discussion mode

---

## 👨‍💻 Developer

**Satyam**

Built as part of an AI Internship project to explore prompt engineering, conversational AI, and modern Python application development.

---

## 📄 License

This project is intended for educational and learning purposes.
