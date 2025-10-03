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
checkpoint_saver= InMemorySaver()
graph.add_node("chat_bot",chat)
graph.add_edge(START,"chat_bot")
graph.add_edge("chat_bot",END)
chatbot= graph.compile(checkpointer=checkpoint_saver)

# while True:
#     user_input=input("Enter your message (or type 'exit' to quit): ")
#     if user_input.lower() in ["exit","quit"]:
#         break
#     initial_state={"messages":[HumanMessage(content=user_input)]}
#     congfig={"configurable":{"thread_id":"first_thread"}}
#     final_state= workflow.invoke(initial_state,config=congfig)
#     print("Bot:",final_state["messages"][-1].content)