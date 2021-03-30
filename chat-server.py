# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, redirect, url_for, request  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/', methods=["GET", "POST"])   # URL '/' to be handled by main() route handler
def main():
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        with open('/app/chat.txt', 'a') as file:
            file.write(mensaje)
    else:
        with open('/app/chat.txt') as file:
            lines = file.readlines()
        return lines


if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
