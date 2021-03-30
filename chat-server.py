# -*- coding: UTF-8 -*-

from flask import Flask, redirect, url_for, request 
import os.path
app = Flask(__name__)   

archivo = "/opt/app-root/src/chat.txt"

@app.route('/', methods=["GET", "POST"]) 
def main():
    if not os.path.exists(archivo):
        with open(archivo, 'w') as fp:
            fp.write("LISTA DE MENSAJES: \n")
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        with open(archivo, 'w+') as file:
            file.write(mensaje)
        return "ok"
    else:
        with open(archivo) as file:
            lines = file.read()
        return lines


if __name__ == '__main__':  
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True) 
