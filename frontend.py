# frontend.py
import requests
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("🤖 AI Chatbot Agents")
st.write("Create and Interact with AI Agents with Stateful Chat!")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("⚙️ Agent Configuration")
    
    system_prompt = st.text_area(
        "Define your AI Agent's personality:", 
        height=100, 
        placeholder="e.g., You are a helpful assistant."
    )

    provider = st.radio("Select Provider:", ("Groq", "OpenAI", "Google"))

    if provider == "Groq":
        selected_model = st.selectbox("Select Groq Model:", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"])
    elif provider == "OpenAI":
        selected_model = st.selectbox("Select OpenAI Model:", ["gpt-4o-mini"])
    elif provider == "Google":
        selected_model = st.selectbox("Select Google Model:", ["gemini-2.5-flash"])

    allow_web_search = st.checkbox("Enable Web Search (via Tavily)", value=True)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- Main Chat Interface ---

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_query := st.chat_input("What would you like to ask?"):

    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    API_URL = "http://127.0.0.1:8000/chat"
    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": st.session_state.messages, 
        "allow_search": allow_web_search
    }
    
    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking..."):
            try:
                response = requests.post(API_URL, json=payload)
                response.raise_for_status()  
                
                response_data = response.json()

                if "error" in response_data:
                    st.error(response_data["error"])
                elif "response" in response_data:
                    final_response = response_data["response"]
                    st.markdown(final_response)
                    st.session_state.messages.append({"role": "assistant", "content": final_response})
                else:
                    st.warning("⚠️ Received an unexpected response format.")

            except requests.exceptions.RequestException as e:
                st.error(f"API Error: Could not connect to the backend. Is it running? \n\nDetails: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
