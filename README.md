# Persona Chatbot with Streamlit

## Overview
This chatbot is a persona-based AI assistant built using Streamlit and OpenAI's NeMo/Mistral model APIs. The chatbot allows users to define a specific character or persona, and it mimics the behavior and dialogue style of that persona during the chat.

## Features
- Allows users to define a persona (e.g., "Sherlock Holmes" or "Dumbledore").
- Provides interactive chat functionality with streaming responses.
- Customizable user interface designed with Streamlit.

## Requirements
To run this project, you need to install the following libraries:

### Python Libraries
- `streamlit` (For building the user interface)
- `openai` (For accessing the API of NeMo/Mistral)

### Installation Commands
You can install the required libraries using pip:

```bash
pip install streamlit openai

## How to Run

1. Clone this repository or download the project files.
2. Navigate to the project directory in your terminal.
3. Run the Streamlit app using the command:

   ```bash
   streamlit run app.py

## Project Structure

- `app.py`: The main Streamlit script for the chatbot.
- `bot_image.jpg`: (Optional) A local image file used for the chatbot's UI (replace with your own image if needed).

---

## Configuration

The API is configured using the following:

```python
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_API_KEY_HERE"
)


