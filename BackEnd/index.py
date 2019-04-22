from main import askMain, readData
from flask import Flask,request
import json

app = Flask(__name__)
# Deklarasi penggunaan Flask

res = readData()
# Membaca file eksternal untuk representasi database

@app.route('/',methods=['POST'])
# Route flask berada pada index, sehingga tidak perlu menjalankan direktori lain untuk menggunakannya

def index() :
    body = request.form # Untuk memasukkan form dari HTML ke python
    selectedalgo = body['algorithm'] # Assign selected algorithm pada HTML ke variabel selected algo
    pat = body['inputbox'] # Assign query pengguna ke dalam variabel pat
    

    result = askMain(pat,res,selectedalgo) # Memanggil fungsi utama untuk string matching
    return json.dumps({'data':result}) # Return dalam bentuk JSON

if __name__ == "__main__":
    # Start Flask
    app.run(debug=True)