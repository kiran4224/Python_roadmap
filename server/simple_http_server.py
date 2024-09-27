import http.server
import socketserver
import os
import sys

import socket

# Get the local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"Local IP Address: {local_ip}")

import argparse
# Create the parser
parser = argparse.ArgumentParser(description="Script to provide bind address and path.")

# Add arguments
parser.add_argument("--port",  default="8000", help="Provide a port number to bind .")
parser.add_argument("--filepath", default= os.getcwd(), help="The file or directory path.")

# Parse the arguments
args = parser.parse_args()
print("command: ",sys.argv)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
os.chdir(args.filepath)  # Replace with your directory path
handler_object = MyHttpRequestHandler
with socketserver.TCPServer(("", int(args.port)), handler_object) as httpd:
    print(f"Serving at port {args.port}")
    print("Server is running. Press Ctrl+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("Server stopped.")
    httpd.server_close()
    print("Server closed.")
