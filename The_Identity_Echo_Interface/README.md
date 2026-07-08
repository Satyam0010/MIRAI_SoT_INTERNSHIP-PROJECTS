# 🛰️ The Identity Echo Interface

A beginner-friendly interactive web application built using **Python** and **Streamlit** as part of the **MirAI School of Technology – Virtual Summer Internship 2026**.

The application demonstrates the fundamentals of frontend development with Streamlit by collecting user input, validating form data, and displaying dynamic responses based on user interactions.

---

## 📌 Project Objective

The primary objective of this project is to understand how Streamlit simplifies web application development by allowing developers to build interactive user interfaces without writing HTML, CSS, or JavaScript.

The application collects multiple user inputs, performs input validation, and conditionally processes data only after an explicit user action.

---

## 🚀 Features

- Interactive web interface built with Streamlit
- User Name input field
- Message input field
- Button-based event handling
- Input validation using conditional statements
- Personalized success response using Python f-strings
- AI Token Consumption Estimator (Optional Challenge)
- Beginner-friendly and easy to extend

---

## 🛠️ Tech Stack

- Python 3
- Streamlit

---

## 📂 Project Workflow

```text
Application Starts
        │
        ▼
Display Title & Instructions
        │
        ▼
Collect User Name
        │
        ▼
Collect User Message
        │
        ▼
Wait for "Transmit" Button
        │
        ▼
────────────────────────────
Was the button clicked?
────────────────────────────
        │
       No
        │
        ▼
Wait for User Interaction

        │
       Yes
        ▼
────────────────────────────
Is Name Empty?
────────────────────────────
        │
     Yes │
        ▼
Display Error Message

        │
      No
        ▼
────────────────────────────
Is Message Empty?
────────────────────────────
        │
     Yes │
        ▼
Display Warning Message

        │
      No
        ▼
Display Personalized Success Message
        │
        ▼
Calculate Character Count
        │
        ▼
Estimate Token Consumption
        │
        ▼
Display System Information
```

---

## 🧠 Concepts Practiced

This project demonstrates the practical implementation of:

- Importing Python Libraries
- Streamlit UI Components
- Variables
- User Input Handling
- Conditional Statements (`if`, `elif`, `else`)
- String Manipulation (`strip()`)
- Built-in Functions (`len()`)
- Python f-Strings
- Event-driven Programming
- Basic AI Token Estimation Logic

---

## 💻 Application Logic

1. Initialize the Streamlit application.
2. Display the application title and instructions.
3. Accept user name and message as input.
4. Wait until the user clicks the **Transmit** button.
5. Validate both input fields.
6. Display appropriate error/warning messages for invalid input.
7. Generate a personalized success message for valid input.
8. Calculate the total number of characters in the message.
9. Estimate token usage using the approximation:

```
1 Token ≈ 4 Characters
```

10. Display the estimated token consumption.

---

## 📸 Preview

> Can Check in Demo Folder

---

## ▶️ Run Locally

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project folder

```bash
cd The_Identity_Echo_Interface
```

Install dependencies

```bash
pip install streamlit
```

Run the application

```bash
streamlit run app.py
```

---

## 📖 Learning Outcomes

After completing this project, I gained hands-on experience with:

- Building interactive web interfaces using Streamlit
- Understanding Streamlit's event-driven execution model
- Handling user inputs and validation
- Creating dynamic responses using Python
- Estimating AI token consumption based on input length
- Developing beginner-friendly web applications without frontend frameworks

---

## 📄 License

This project was developed for educational purposes as part of the **MirAI School of Technology – Virtual Summer Internship 2026**.