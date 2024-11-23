from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello platanus first commit!"


@app.route('/query', methods=['POST'])
def query():
    ...


if __name__ == '__main__':
    app.run(debug=True)
