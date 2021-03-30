# -*- coding: UTF-8 -*-

from flask import Flask, redirect, url_for, request 
import os.path
app = Flask(__name__)   

@app.route('/', methods=["GET", "POST"]) 
def main():
    if not os.path.exists("chat_lines.txt"):
        os.touch("chat_lines.txt")
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        with open("chat_lines.txt", 'w+') as file:
            file.write(mensaje)
        return "ok"
    else:
        with open("chat_lines.txt") as file:
            lines = file.read()
        return lines


if __name__ == '__main__':  
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True) 
