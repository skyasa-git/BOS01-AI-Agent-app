import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="BOS01 AI Agent", page_icon="🤖")
st.title("🤖 BOS01 AI Agent")
st.caption("AI-powered assistant for data center operations")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

generator = load_model()

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
            result = generator(prompt, max_length=150, num_return_sequences=1, do_sample=True, temperature=0.7)
            response = result[0]["generated_text"]
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})