from http.server import BaseHTTPRequestHandler
from urllib import parse
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        if "name" in dic:
            message = "Hello, " + dic["name"] + "!"
        else:
            message = "Hello, stranger!"
        self.wfile.write(message.encode())
        return

# from http.server import BaseHTTPRequestHandler
# from cowpy import cow

# class handler(BaseHTTPRequestHandler):
  
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
#         self.wfile.write(message.encode())
#         return