from traceloop.sdk import Traceloop
import os
import openai

Traceloop.init(app_name="openai-obs", disable_batch=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])



