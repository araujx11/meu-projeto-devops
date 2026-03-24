from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "mensagem": "API DevOps funcionando!",
        "ambiente": os.getenv("AMBIENTE", "desenvolvimento")
    })

@app.route("/saude")
def saude():
    return jsonify({"status": "saudavel"}), 200

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    porta = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=porta, debug=False)