
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

name = os.getenv("NAME", "World")

class BankingApp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = f"""
        <h1>Banking Application Started</h1>
        <h2>Hello {name}!</h2>
        <p>Application is running successfully.</p>
        """
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 5000), BankingApp)

print("Banking Application Started on port 5000")

server.serve_forever()
