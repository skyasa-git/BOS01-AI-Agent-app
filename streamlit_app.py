import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="BOS01 AI Agent", page_icon="🤖")
st.title("🤖 BOS01 AI Agent")
st.caption("AI-powered assistant for data center operations")

client = InferenceClient()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about data center operations..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.text_generation(prompt, model="gpt2", max_new_tokens=150)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})