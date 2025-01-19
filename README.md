#Persona Chatbot with Streamlit

Overview

This chatbot is a persona-based AI assistant built using Streamlit and OpenAI's NeMo/Mistral model APIs. The chatbot allows users to define a specific character or persona, and it mimics the behavior and dialogue style of that persona during the chat.

Features

Allows users to define a persona (e.g., "Sherlock Holmes" or "Dumbledore").

Provides interactive chat functionality with streaming responses.

Customizable user interface designed with Streamlit.

Requirements

To run this project, you need to install the following libraries:

Python Libraries

streamlit (For building the user interface)

openai (For accessing the API of NeMo/Mistral)

Installation Commands

You can install the required libraries using pip:
pip install streamlit openai



How to Run

Clone this repository or download the project files.

Navigate to the project directory in your terminal.

Run the Streamlit app using the command:
streamlit run app.py

Open the app in your browser at http://localhost:8501 (this will automatically open).



Project Structure

app.py: The main Streamlit script for the chatbot.

bot_image.jpg: (Optional) A local image file used for the chatbot's UI (replace with your own image if needed).

Configuration

The API is configured using the following:
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_API_KEY_HERE"
)
Replace YOUR_API_KEY_HERE with your valid NVIDIA/OpenAI API key.



How to Use

Enter a persona in the "Choose a Persona" input box (e.g., "Sherlock Holmes").

Type your message in the input field and press Enter.

The chatbot will respond as if it were the chosen persona.

Known Issues

Ensure the API key is valid and has sufficient access rights.

If using a local image, verify the file path is correct and the image exists.

For online images, check that the image URL is valid and accessible.

License

This project is intended for educational purposes and is licensed under an open-source license. Feel free to modify and distribute it as needed.

Acknowledgments

Streamlit: For the lightweight and powerful UI framework.

OpenAI NeMo: For the robust model APIs.

NVIDIA: For providing the Mistral model.



