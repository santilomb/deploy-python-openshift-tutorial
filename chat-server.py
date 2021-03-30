# -*- coding: UTF-8 -*-

from flask import Flask, redirect, url_for, request 
app = Flask(__name__)   

@app.route('/', methods=["GET", "POST"]) 
def main():
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        with open('/tmp/chat.txt', 'a') as file:
            file.write(mensaje)
        return "ok"
    else:
        with open('/tmp/chat.txt') as file:
            lines = file.read()
        return lines


if __name__ == '__main__':  
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True) 
