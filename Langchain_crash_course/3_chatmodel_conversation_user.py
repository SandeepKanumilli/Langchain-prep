from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage,AIMessage

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API')

model = ChatOpenAI(
    model = "gpt-4o",
    api_key=api_key
)

chat_history = []

system_message = SystemMessage("You are a helpful AI Assistent!")

chat_history.append(system_message)


while True:
    query = input("You : ")
    if query.lower() == "exit":
        break
    human_message = HumanMessage(content = query)
    chat_history.append(human_message)
    
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print(response.content)


print("chat History: ")
print(chat_history)
     


