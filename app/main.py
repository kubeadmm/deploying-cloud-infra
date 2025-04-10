from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to dhaka Final Test API Server"

@app.route('/host')
def host():
    return socket.gethostname()

@app.route('/ip')
def ip():
    return socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Changed to 0.0.0.0