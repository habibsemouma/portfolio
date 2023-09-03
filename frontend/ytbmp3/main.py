from flask import Flask, jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:5173')
@app.route('/audio', methods=['GET','POST'])
def get_url():
    data=request.json
    url=data['url']
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
