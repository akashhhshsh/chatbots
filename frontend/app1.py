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


# Sidebar customization
with st.sidebar:
    st.title("⚙️ Chatbot Settings")
    character = st.text_input("Persona (e.g., Jarvis from Iron Man):", "Jarvis from Iron Man")
    st.markdown(
        """
        **Instructions**:  
        - Enter a persona for the chatbot to mimic.  
        - Start chatting below!
        """
    )

# Main UI layout
st.title("🤖 Persona Chatbot")
st.markdown("**Chat with a custom persona-powered AI assistant!**")

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
prompt = st.chat_input("Ask your question here...")

# If user provides input
if prompt:
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"**You:** {prompt}")

    # Generate response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()  # Create a placeholder for streaming
        full_response = ""  # Initialize an empty string to store the full response

        # Stream the response chunks
        stream = get_stream(prompt, character)
        for chunk in stream:
            if hasattr(chunk, "choices") and chunk.choices:  # Check if 'choices' exists
                delta = chunk.choices[0].delta  # Extract the delta (streamed token data)
                if hasattr(delta, "content") and delta.content:
                    full_response += delta.content  # Append the content to the response
                    response_placeholder.markdown(full_response, unsafe_allow_html=True)

    # Append assistant's final response to session state
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer styling
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    footer:after {
        content:'Developed by [Your Name] | Powered by NVIDIA NeMo & OpenAI';
        visibility: visible;
        display: block;
        text-align: center;
        font-size: small;
        color: gray;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
