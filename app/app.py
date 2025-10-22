from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    msg = os.getenv("APP_MESSAGE", "Hello from AKS!")
    return jsonify({"message": msg})

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
