import ollama
import streamlit as st

st.title("🤖 My AI Chatbot")
st.markdown(" 💬 Welcome to your personal AI assistant!")
st.markdown(" *✨ Ask questions • 📚 Study • 💡 Explore • 😂 Have fun*")
with st.sidebar:
    st.header("⚙️ Chat Settings")

    st.markdown("### 🎭 Assistant Personality")

    personality = {
        "📚 Study Assistant": "You are a friendly and helpful assistant.",
        "😂 Humorous": "You are a humorous and witty assistant.",
        "🔎 Inquisitive": "You are an inquisitive and curious assistant."
    }

    personality = st.selectbox(
        "*Select the personality of the assistant*",
        personality.keys()
    )

    st.markdown("### 📁 File Upload")

    uploaded_file = st.file_uploader(
        "*Select the file you want to upload*"
    )

    try:
        if uploaded_file:
            st.success("✅ File uploaded successfully!!")

            content = uploaded_file.read().decode("utf-8")

            if st.button("👀 Display"):
                st.text(content)

    except:
        st.error("❌ Error reading the file. Please ensure it's a valid text file.")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.success("Chat history deleted!")


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


question = st.chat_input("💭 Ask me anything...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    with st.spinner("🧠 Thinking..."):

        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": personality
                }
            ] + st.session_state.messages
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response["message"]["content"]
        }
    )

    with st.chat_message("assistant"):
        st.write(response["message"]["content"])