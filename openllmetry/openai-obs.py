from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow, task
import os
import openai
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

Traceloop.init(app_name="openai-obs", disable_batch=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

class MyServer(BaseHTTPRequestHandler):
    @task(name="retrieve_docs")
    def llm_request(self):
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    @workflow(name="ask_question")
    def do_GET(self):
        self.llm_request()
        self.wfile.write(bytes("Ok", "utf-8"))
        
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")