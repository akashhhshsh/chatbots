import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="Persona Chatbot", page_icon="🤖")

# Custom CSS with fixed footer and improved sidebar visibility
st.markdown("""
    <style>
    /* Main app background */
    .stApp {
        background-color: white;
    }
    
    /* Footer styling */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #f0f2f6;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        font-size: 16px;
        color: #000000;
        border-top: 2px solid #e0e0e0;
        z-index: 1000;
    }
    
    /* Improved sidebar styling */
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    
    /* Custom container for sidebar content */
    .sidebar-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    
    .sidebar-title {
        color: #000000;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    
    .sidebar-text {
        color: #000000;
        font-size: 16px;
        line-height: 1.6;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background-color: #f0f2f6;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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",
)

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

# Sidebar with improved visibility
with st.sidebar:
    st.image("/Users/akashadhyapak/Documents/ML/chatbots/frontend/chatbot.png", use_container_width=True)
    
    # Chat Settings Title
    st.markdown("""
        <div class="sidebar-box">
            <div class="sidebar-title">Chat Settings 🛠️</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Character Input
    character = st.text_input(
        "Enter Persona (e.g., Hermione Granger):", "Hermione Granger"
    )
    
    # Instructions
    st.markdown("""
        <div class="sidebar-box">
            <div class="sidebar-text">
                <strong>Customize your experience:</strong><br>
                • Specify a persona for the chatbot<br>
                • Type your queries below!
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main UI layout
st.markdown("<h1 style='color: #000000;'>🤖 Persona Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #000000;'><strong>Chat with your chosen persona below:</strong></p>", unsafe_allow_html=True)

# Display chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f"<div style='color: #000000;'>{message['content']}</div>", unsafe_allow_html=True)

# User input section
st.markdown(
    """
    <p style="color: #000000; font-size: 18px; font-weight: bold; margin-bottom: 5px;">
    Type your message here 👇
    </p>
    """,
    unsafe_allow_html=True,
)
prompt = st.chat_input("")

# Handle user input
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: #000000;'><strong>You:</strong> {prompt}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        stream = get_stream(prompt, character)
        for chunk in stream:
            if hasattr(chunk, "choices") and chunk.choices:
                delta = chunk.choices[0].delta
                if hasattr(delta, "content") and delta.content:
                    full_response += delta.content
                    response_placeholder.markdown(
                        f"<div style='color: #000000;'>{full_response}</div>",
                        unsafe_allow_html=True
                    )

    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Fixed footer with improved visibility
st.markdown("""
    <div class="footer">
        Developed by Shruti Patodia | Powered by NVIDIA NeMo & OpenAI
    </div>
""", unsafe_allow_html=True)

# Add padding at the bottom to prevent content from being hidden by footer
st.markdown("<div style='margin-bottom: 80px;'></div>", unsafe_allow_html=True)