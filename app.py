from flask import Flask, jsonify
from flask_cors import CORS   # lets the frontend fetch us from :3000

app = Flask(__name__)
CORS(app)                      # enable CORS for all routes

@app.route("/api/message")
def message():
    return jsonify({"message": "Hello from Flask backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
