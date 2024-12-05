import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API')
print(api_key)
llm = ChatOpenAI(
    model = "gpt-4o",
    api_key=api_key
    )


message = [
    (
        "system",
        "You are an useful assisatant in writing jokes about AI. so tell me three jokes about AI"
    )
    
]


ai_message = llm.invoke(message)
print(ai_message)
print("Hello World")




 









# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI

# import openai

# load_dotenv()



# model = ChatOpenAI(model="gpt-3.5")


# result = model.invoke("Whats the most complicated language in the world? and say hoello in that language!")
# print(result.content)

# api_key = "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"

# from openai import OpenAI
# client = OpenAI(api_key=api_key)

# def answer(client):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": "Write a haiku about recursion in programming."
#             }
#         ]
#     )
    
# return response.choices[0].message.content.strip()

# output = answer(client)