# backend.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from agent import get_response_from_ai_agent 

app = FastAPI(title="LangGraph AI Agent")


ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant", 
    "gpt-4o-mini",
    "gemini-1.5-flash-latest"
]

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    allow_search: bool

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}

    response = get_response_from_ai_agent(
        request.model_name,
        request.messages,
        request.allow_search,
        request.system_prompt,
        request.model_provider
    )
    
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
