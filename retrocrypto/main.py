from flask import Flask, jsonify, request,send_file
from flask_cors import CORS
from utils import *
from werkzeug.utils import secure_filename
import io

app = Flask(__name__)
CORS(app, origins="*")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/traditional", methods=["GET", "POST"])
def get_items():
    data = request.json

    if data["encoding"] == "atbash":
        if data["type"] == "encode":
            response = {"text": atbash_encode(data["text"])}
        elif data["type"] == "decode":
            response = {"text": atbash_decode(data["text"])}

    elif data["encoding"] == "caesar":
        if data["type"] == "encode":
            response = {"text": caesar_encode(data["text"], int(data["shift"]))}
        elif data["type"] == "decode":
            response = {"text": caesar_decode(data["text"], int(data["shift"]))}

    elif data["encoding"] == "railfence":
        if data["type"] == "encode":
            response = {"text": railfence_encode(data["text"], int(data["rails"]))}
        elif data["type"] == "decode":
            response = {"text": railfence_decode(data["text"], int(data["rails"]))}

    elif data["encoding"] == "vigenere":
        if data["type"] == "encode":
            response = {"text": vigenere_encode(data["text"], data["keyword"])}
        elif data["type"] == "decode":
            response = {"text": vigenere_decode(data["text"], data["keyword"])}

    return jsonify(response)

app.route("/stenhide",methods=["POST"])
def stendhide():
    data = request.json
    img=request.files['image']
    if img and allowed_file(file.filename):
        filename = secure_filename(file.filename)
            
    if data["type"] == "embed":
        plaintext=data["plaintext"]
        mod_img=embed_text(plaintext,img)
        img_buffer=io.BytesIO()
        img.save(img_buffer,format="png")
        img_buffer.seek(0)
        return send_file(img_buffer,mimetype="image/png")

    elif data["type"]=="extract":
        pass
    

if __name__ == "__main__":
    app.run()
