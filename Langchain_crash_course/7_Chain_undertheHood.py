import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

api_key = os.getenv('OPENAI_API')

llm = ChatOpenAI(
    model = 'gpt-3.5-turbo',
    api_key=api_key
)

message = ChatPromptTemplate.from_messages([
    ("system : You are an helpful AI Assitant, you're job is to indicate, How the career progression of an  {role} "),
    ("human : In the span of next {years} down the line")
])

# Define each function
prompt_template = RunnableLambda(lambda x : message.format_prompt(**x))
model_invoke = RunnableLambda(lambda x : llm.invoke(x.to_messages()) )
str_parser = RunnableLambda( lambda x : x.content)

# Running multiple functions in a sequence
chain = RunnableSequence(first= prompt_template, middle=[model_invoke], last=str_parser)

result = chain.invoke({"role" : "AI Engineer" , "years" : "10"})

print(result)
 