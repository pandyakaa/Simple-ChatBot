from BM import BMmain
from KMP import KMPmain
from regex import regexmain
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index() :
    body = request.form['inputbox']
    return json.dumps({'data':body})

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')