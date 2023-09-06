from flask import Flask, jsonify,request
from flask_cors import CORS
from utils import *

app = Flask(__name__)
CORS(app, origins='*')
@app.route('/traditional', methods=['GET','POST'])
def get_items():
    data=request.json
    if data["encoding"]=="atbash":
        if data["type"]=="encode": response= {'text':atbash_encode(data["text"])}
        elif data["type"]=="decode": response= {'text':atbash_decode(data["text"])}
    
    elif data["encoding"]=="caesar":
        if data["type"]=="encode": response= {'text':caesar_encode(data["text"],int(data['shift']))}
        elif data["type"]=="decode": response= {'text':caesar_decode(data["text"],int(data['shift']))}
    
    elif data["encoding"]=="railfence":
        if data["type"]=="encode": response={'text':railfence_encode(data['text'],int(data["rails"]))}
        elif data["type"]=="decode": response={'text': railfence_decode(data["text"],int(data["rails"]))}

    elif data["encoding"]=="vigenere":
        if data["type"]=="encode": response={"text":vigenere_encode(data["text"],data["keyword"])}
        elif data["type"]=="decode": response={"text":vigenere_decode(data["text"],data["keyword"])}

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
