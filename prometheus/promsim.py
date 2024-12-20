from http.server import BaseHTTPRequestHandler, HTTPServer
import random

prometheus_paths = [f"/api/v1/resource/{i}" for i in range(1, 700)]

def generate_service_payload(path):
    # Some random services numbers
    DURATION_GET_BUCKET_1 = random.randint(1, 10)
    DURATION_GET_BUCKET_2 = random.randint(1, 20)
    DURATION_GET_BUCKET_3 = random.randint(1, 30)
    DURATION_GET_BUCKET_4 = random.randint(1, 30)
    DURATION_GET_BUCKET_5 = random.randint(1, 20)
    DURATION_GET_BUCKET_6 = random.randint(1, 10)

    REQUESTS_TOTAL_GET = DURATION_GET_BUCKET_1 + DURATION_GET_BUCKET_2 + DURATION_GET_BUCKET_3 + DURATION_GET_BUCKET_4 + DURATION_GET_BUCKET_5 + DURATION_GET_BUCKET_6 
    REQUESTS_TOTAL_POST = random.randint(1, 100)
    
    DURATION_GET_SECONDS_SUM = REQUESTS_TOTAL_GET * 0.5
    REQUESTS_TOTAL_GET_ERRORS_500 = 0
    REQUESTS_TOTAL_POST_ERRORS_400 = 0

    # Open the file in read mode
    with open('templates/service.prom', 'r') as file:
        # Read the contents of the file
        prom_template = file.read()
        prom_string = prom_template.replace('?PATH?', path).replace('?REQUESTS_TOTAL_GET?', str(REQUESTS_TOTAL_GET)).replace('?REQUESTS_TOTAL_POST?', str(REQUESTS_TOTAL_POST)).replace('?DURATION_GET_SECONDS_SUM?', str(DURATION_GET_SECONDS_SUM)).replace('?REQUESTS_TOTAL_GET_ERRORS_500?', str(REQUESTS_TOTAL_GET_ERRORS_500)).replace('?REQUESTS_TOTAL_POST_ERRORS_400?', str(REQUESTS_TOTAL_POST_ERRORS_400)).replace('?DURATION_GET_BUCKET_1?', str(DURATION_GET_BUCKET_1)).replace('?DURATION_GET_BUCKET_2?', str(DURATION_GET_BUCKET_2)).replace('?DURATION_GET_BUCKET_3?', str(DURATION_GET_BUCKET_3)).replace('?DURATION_GET_BUCKET_4?', str(DURATION_GET_BUCKET_4)).replace('?DURATION_GET_BUCKET_5?', str(DURATION_GET_BUCKET_5)).replace('?DURATION_GET_BUCKET_6?', str(DURATION_GET_BUCKET_6))
        #print(prom_string)
        return prom_string


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        payload = ""
        # Iterate through the array and print each item
        for path in prometheus_paths:
            payload = payload + "\n" + generate_service_payload(path)
        
        self.wfile.write(bytes(payload, 'utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 9000)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd server on port 9000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
