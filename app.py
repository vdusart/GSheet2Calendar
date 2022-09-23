import os
from http.server import HTTPServer, CGIHTTPRequestHandler

app = HTTPServer(server_address=('', 8080), RequestHandlerClass=CGIHTTPRequestHandler)

if __name__ == '__main__':
    os.chdir('.')
    app.serve_forever()
