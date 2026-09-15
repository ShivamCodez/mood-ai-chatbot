import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# Load environment variables
load_dotenv()

# Initialize model
model = ChatMistralAI(model="mistral-large-2512")

# Page Config
st.set_page_config(
    page_title="Funny AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Funny AI Chatbot")

# Initialize chat history
if "message_history" not in st.session_state:
    st.session_state.message_history = [
        SystemMessage(content="you are a funny AI agent")
    ]

# Display previous messages (except system message)
for message in st.session_state.message_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Store user message
    st.session_state.message_history.append(
        HumanMessage(content=prompt)
    )

    # Get response
    response = model.invoke(st.session_state.message_history)

    # Store AI response
    st.session_state.message_history.append(
        AIMessage(content=response.content)
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)