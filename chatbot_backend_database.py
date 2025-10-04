from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langgraph.graph import StateGraph,START, END
from typing import TypedDict, Literal, Annotated,Literal
from langchain_core.messages import SystemMessage, HumanMessage,BaseMessage
import operator
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()

bot = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]
def chat(state: ChatState) -> ChatState:
    message_history=state["messages"]
    response=bot.invoke(message_history)
    return {"messages":[response]}  

graph=StateGraph(ChatState)

graph.add_node("chat_bot",chat)
graph.add_edge(START,"chat_bot")
graph.add_edge("chat_bot",END)

conntection_object=sqlite3.connect('chatbot.db',check_same_thread=False)
checkpoint_saver= SqliteSaver(conntection_object)
chatbot= graph.compile(checkpointer=checkpoint_saver)


def retrieve_threads():
    thread_set=set()
    checkpoints=checkpoint_saver.list(None)
    for checkpoint in checkpoints:
        thread_set.add(checkpoint.config['configurable']['thread_id'])
    return list(thread_set)


