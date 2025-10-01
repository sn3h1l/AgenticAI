import streamlit as st
from chatbot_backend import workflow
from langchain_core.messages import SystemMessage, HumanMessage,BaseMessage

# the imported workflow object is the compiled graph from chatbot_backend.py


if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


for messages in st.session_state["message_history"]:
    with st.chat_message(messages["role"]):
        st.text(messages["content"])


CONFIG={"configurable":{"thread_id":"thread_1"}}



#st.chat_input --> handles taking input from user (streamlit component) in the UI
#st.chat_message("User") --> displays a user message (streamlit chat component)
#st.chat_message("Assistant") --> displays an assistant's response  (streamlit chat component)


user_input = st.chat_input("Type your message here")

if user_input:
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    node_state = {"messages": [HumanMessage(content=user_input)]}
    final_state = workflow.invoke(node_state, config=CONFIG)
    bot_response = final_state["messages"][-1].content
    st.session_state["message_history"].append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.text(bot_response)

