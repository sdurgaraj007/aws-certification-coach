# Import required packages
import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = os.environ.get("OPENAI_API_KEY")

# Choose the model
if "model" not in st.session_state:
    st.session_state["model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("AWS Certfication Coach")

# Display previous messages in app reinitialised
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
input = st.chat_input("User: ")

if input:
    # Display user input in chat container
    with st.chat_message("user"):
        st.markdown(input)

    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": input})

    # Display assistant response in chat container
    with st.chat_message("assistant"):
        # Generate response from OpenAI
        stream = client.chat.completions.create(
            model=st.session_state["model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
        # Add assistant response to chat history
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
