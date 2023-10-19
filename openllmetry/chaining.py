from traceloop.sdk import Traceloop
import os
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

Traceloop.init(app_name="openai-obs", disable_batch=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai.api_key)

chat_model = ChatOpenAI()

prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")
model = ChatOpenAI()
chain = prompt | model

print(chain.invoke({"foo": "bears"}))