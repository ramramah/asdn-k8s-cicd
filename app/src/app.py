from flask import Flask, request, jsonify

app = Flask(__name__)

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
        version="1.0.0",
        description="Simple HTTP network service for CI/CD on Kubernetes"
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
