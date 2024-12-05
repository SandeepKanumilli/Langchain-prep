import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_openai import ChatOpenAI


load_dotenv()

api_key = os.getenv('OPENAI_API')


llm = ChatOpenAI(
    model = 'gpt-4o',
    api_key=api_key
)

template = "system : You are an helpful AI assitent, which helps us finding the root of the word -{word}"

prompt01 = ChatPromptTemplate.from_template(template)

#prompt = prompt01.invoke({"word" : "Orange"})


chain = prompt01 | llm | StrOutputParser()

result = chain.invoke({"word" : "Orange"})
print(result)

#StrOutputParser basically prints output , instead of using result.invoke






