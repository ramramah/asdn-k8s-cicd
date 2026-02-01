from flask import Flask, request, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.1")   # changed from 1.0.0

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

@app.route("/echo", methods=["GET"])
def echo():
    message = request.args.get("msg", "hello")
    return jsonify(message=message), 200

@app.route("/info", methods=["GET"])
def info():
    return jsonify(
        app="ASDN Network Service",
        version=APP_VERSION,
        description="ASDN service - pipeline test 1.0.2"
    ), 200

# NEW endpoint to verify new deployment easily
@app.route("/build", methods=["GET"])
def build():
    return jsonify(
        version=APP_VERSION,
        git_commit=os.getenv("GIT_COMMIT", "unknown"),
        build_number=os.getenv("BUILD_NUMBER", "local")
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
