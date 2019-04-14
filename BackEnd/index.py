from main import *
from flask import Flask,request
import json

app = Flask(__name__)

res = readData()

def findAnswer(pat,res,method) :
    askMain(pat,res,method)

@app.route('/',methods=['POST'])
def index() :
    body = request.form
    selectedalgo = body['algorithm']
    pat = body['inputbox']

    result = askMain(pat,res,selectedalgo)
    return json.dumps({'data':result})

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')