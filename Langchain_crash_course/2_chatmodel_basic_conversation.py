from langchain_openai import ChatOpenAI 
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API')
print(api_key)
model = ChatOpenAI(
    model = "gpt-4o",
    api_key=api_key
)

message = [
    SystemMessage("Solve the math or logic problems!"),
    HumanMessage("There are two ducks in front of a duck, two ducks behind a duck and a duck in the middle. How many ducks are there?")
]

result = model.invoke(message)
print(result.content)




