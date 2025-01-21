import streamlit as st
from openai import OpenAI

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
                "content": f"""You're chat assistant which chats as specified character.
                            You have to talk as you're this character : {character}
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


with st.sidebar:
    option = st.selectbox(
        "Choose your model :",
        ("Mistral", "Llama"),
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("Persona Chatbot")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Say something")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = get_stream(prompt, "Jarvis from iron man")
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})