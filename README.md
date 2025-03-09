🤖 AI Chatbot Agents
🚀 An interactive AI chatbot powered by Groq & OpenAI models, with optional web search integration, and a sleek Streamlit UI!

✨ Features
✅ Multiple AI Models – Supports Llama 3, Mixtral, and GPT-4o


✅ FastAPI Backend – High-performance API handling


✅ Streamlit UI – Simple and interactive frontend


✅ Web Search Integration – Uses Tavily API for real-time search


✅ Dynamic Model Selection – Choose between Groq & OpenAI


✅ Easily Deployable – Can be hosted on Streamlit Cloud, Render, Railway, Fly.io



🛠 Technologies Used


🔹 Python – Core programming language


🔹 FastAPI – Lightweight backend framework


🔹 Streamlit – UI framework for interactive apps


🔹 LangGraph – AI agent framework


🔹 Groq API – For Llama 3 & Mixtral models


🔹 OpenAI API – For GPT models


🔹 Tavily API – Enables web search


🔹 Uvicorn – ASGI server for FastAPI


💻 How to Run Locally


1️⃣ Clone the Repository

```
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

2️⃣ Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```
3️⃣ Install Dependencies

```pip install -r requirements.txt```


4️⃣ Set Up Environment Variables


Create a .env file and add your API keys:

```
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```
5️⃣ Start the Backend Server

```uvicorn backend:app --host 127.0.0.1 --port 8000 --reload```


6️⃣ Run the Streamlit UI

```streamlit run frontend.py```

Now, open your browser and go to http://localhost:8501 to chat with the AI agent! 🎉

📢 Future Enhancements
🚀 Support for more AI models
🚀 Deploy on cloud platforms
🚀 Multi-agent interactions

