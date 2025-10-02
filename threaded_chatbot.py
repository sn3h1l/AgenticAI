import streamlit as st
from chatbot_backend import workflow
from langchain_core.messages import SystemMessage, HumanMessage,BaseMessage
import uuid
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


#*************** UTILILTY FUNCTIONS *************************

def add_new_thread():
    st.session_state["thread_id"] = str(uuid.uuid4())

#************************SIDEBAR UI**************************

st.sidebar.title("Threaded Chatbot")

if st.sidebar.button("Start a new chat"):
    add_new_thread()
    st.session_state["message_history"] = []
    
st.sidebar.text("THREAD IDS")
#************************MAIN UI PART*************************
for messages in st.session_state["message_history"]:
    with st.chat_message(messages["role"]):
        st.text(messages["content"])


CONFIG={"configurable":{"thread_id":"thread_1"}}

user_input = st.chat_input("Type your message here")

if user_input:
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    node_state = {"messages": [HumanMessage(content=user_input)]}
    with st.chat_message("assistant"):
        workflow_response = st.write_stream(message.content for message,metadata in workflow.stream(node_state,config=CONFIG,stream_mode="messages"))
    st

# the st.write stream component streams the response in the UI part and the workflow.stream method streams the response from the flash API in two parts message and metadata