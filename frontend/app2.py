import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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",
)

# Function to get responses from the model
def get_stream(prompt, character):
    completion = client.chat.completions.create(
        model="nv-mistralai/mistral-nemo-12b-instruct",
        messages=[
            {
                "role": "user",
                "content": f"""You're a chat assistant which chats as a specified character.
                            You have to talk as if you're this character: {character}
                            <user query>
                            {prompt}
                            <user query>
                            """,
            }
        ],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True,
    )
    return completion


# Sidebar and Page Config
st.set_page_config(page_title="Persona Bot", page_icon="🤖", layout="wide")

# Sidebar for Persona Selection
with st.sidebar:
    st.image("/Users/akashadhyapak/Documents/ML/chatbots/frontend/chatbot.png", width=150)  # Replace with an actual image
    st.title("Persona Bot 🤖")
    character = st.text_input(
        "Choose a Persona",
        placeholder="Enter a persona (e.g. Sherlock Holmes)",
        help="Define the character the chatbot will mimic.",
    )
    st.markdown(
        """
        - Define a persona for the bot.  
        - Start chatting below!
        """,
        unsafe_allow_html=True,
    )


# Header and Introduction Section
st.markdown(
    """
    <div style="text-align: center; background-color: #4A4A4A; padding: 20px; border-radius: 10px; margin-bottom: 20px; color: white;">
        <h1 style="margin: 0;">Welcome to Persona Bot 🤖</h1>
        <p>Chat with an AI assistant customized to your favorite persona!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Display Area
chat_area = st.container()

# Display Previous Messages
with chat_area:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}", unsafe_allow_html=True)
        else:
            st.markdown(f"**{character or 'Your Assistant'}:** {message['content']}", unsafe_allow_html=True)

# Input Section
prompt = st.text_input(
    "Type your message here",
    placeholder="Ask something to your assistant...",
    key="user_input",
)

# Process User Input
if prompt:
    # Add user input to session messages
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_area:
        st.markdown(f"**You:** {prompt}", unsafe_allow_html=True)

    # Get Assistant Response
    full_response = ""
    response_placeholder = st.empty()
    stream = get_stream(prompt, character or "Your Assistant")
    for chunk in stream:
        if hasattr(chunk, "choices") and chunk.choices:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                full_response += delta.content
                response_placeholder.markdown(full_response, unsafe_allow_html=True)

    # Add assistant response to session messages
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: small; padding: 20px; border-top: 1px solid #ddd;">
        Developed by Arsh Gopani. Powered by NVIDIA NeMo & OpenAI.
    </div>
    """,
    unsafe_allow_html=True,
)
