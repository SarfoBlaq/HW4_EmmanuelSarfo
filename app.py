from flask import Flask, jsonify
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

@app.route ('/covid')
def tracker():
      data = dict(
            newcses=26,
            total=43,
            recvrd=67,
            actvcses=77,
            totald=34)
      return jsonify(data)
