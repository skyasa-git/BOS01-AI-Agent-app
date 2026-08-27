import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="BOS01 AI Agent", page_icon="🧠")
st.title("🧠 BOS01 AI Agent")
st.caption("👤 Created by Sai Kyasa | ⚡ Powered by NVIDIA CUDA | Phi-2 Model")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="microsoft/phi-2")

bot = load_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    result = bot(f"User: {prompt}\nAssistant:", max_new_tokens=200, do_sample=True)
    reply = result[0]['generated_text'].split("Assistant:")[-1].strip()

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)