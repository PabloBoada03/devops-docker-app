from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify(message="¡Hola desde DevOps + Docker!")

@app.get("/health")
def health():
    return jsonify(status="ok")
