from flask import Flask
import os

app = Flask(__name__)


@app.route("/", methods=["POST"])
def post_request():
    try:
        return "Hello world (POST)"
    except Exception as e:
        print(str(e))
        raise Exception(e)


@app.route("/", methods=["GET"])
def get_request():
    try:
        return "Hello world (GET)"
    except Exception as e:
        print(str(e))
        raise Exception(e)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
