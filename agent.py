# agent.py
from dotenv import load_dotenv
load_dotenv()
import os

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def get_response_from_ai_agent(llm_id, query_messages, allow_search, system_prompt, provider):
    """
    Initializes an AI agent and gets a response.
    """
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, temperature=0)
    elif provider == "Google":
        llm = ChatGoogleGenerativeAI(model=llm_id)
    else:
        raise ValueError("Invalid provider specified.")

    tools = [TavilySearch(max_results=3)] if allow_search else []
    
    if system_prompt and system_prompt.strip():
        enhanced_system_prompt = (
            "You are an assistant with access to a web search tool. "
            "You must use this tool to find current information (like today's date, weather) or any other information you do not possess. "
            "After using the tool, answer the user's question based on the results.\n\n"
            "Here is your primary personality from the user:\n"
            f"'{system_prompt}'"
        )
    else:
        enhanced_system_prompt = (
            "You are a helpful assistant with access to a web search tool. "
            "Use it to answer questions about current events, real-time information (like today's date), or any other topic you need to look up."
        )

    messages = [SystemMessage(content=enhanced_system_prompt)]
    
    for msg in query_messages:
        if msg.get("role") == "user":
            messages.append(HumanMessage(content=msg.get("content")))
        elif msg.get("role") == "assistant":
            messages.append(AIMessage(content=msg.get("content")))

    agent_executor = create_react_agent(model=llm, tools=tools)
    
    state = {"messages": messages}
    response = agent_executor.invoke(state)

    final_response_message = response.get("messages", [])[-1]
    final_response = final_response_message.content if final_response_message else "**No response from AI.**"

    if allow_search:
        tool_was_used = any(
            isinstance(msg, AIMessage) and msg.tool_calls for msg in response.get("messages", [])
        )
        if tool_was_used:
             final_response += "\n\n*(A web search was conducted to answer this question.)*"
    
    return {"response": final_response}
