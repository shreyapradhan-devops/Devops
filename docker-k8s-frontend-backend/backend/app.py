from flask import Flask,jsonify
from flask_cors import CORS
import socket

app=Flask(__name__)
CORS(app)

@app.route("/api/info")

def info():
    return jsonify({"app":"Devops Dashboard", "hostname":socket.gethostname(),"status":"Running in Kubernetes"})

if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=5000)

