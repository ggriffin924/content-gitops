from flask import Flask
app = Flask(__name__)
# Simple hello world for deployment to kubernetes pod
# Linux Accademy testing CI/CD pipelines
# Test001a


@app.route("/")
def hello():
    return "Hello Griffin QA and the World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
