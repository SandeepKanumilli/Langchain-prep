from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API')
#PROJECT_ID = "langchaincrashcourse-6b764"
PROJECT_ID = "langchaincrashcourse-443420"
SESSION_ID = "Session_001"
COLLECTION_NAME = "Chat_History"

print("Initializing Firestore Database!!!!")
client = firestore.Client(project = PROJECT_ID)

print("Initializing fire store chat hisotry!")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection= COLLECTION_NAME,
    client= client
)  

print("Chat History Intiallized!")
print("Chat History so far :")
print(chat_history.messages)


llm = ChatOpenAI(
    model = "gpt-4o",
    api_key=api_key
)

while True:
    query = input("YOU :")
    if query.lower() == "exit":
        break
    chat_history.add_user_message(query)
    response = llm.invoke(chat_history.messages)
    chat_history.add_ai_message(response.content)
    print(f"AI: {response.content}")