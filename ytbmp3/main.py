from flask import Flask, jsonify,request,send_file
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS
from utils import *

scheduler = BackgroundScheduler(daemon=True)
scheduler.start()
app = Flask(__name__)
CORS(app, origins='*')
@app.route('/audio', methods=['GET','POST'])
def get_url():
    data=request.json
    url=data['url']
    filename,video_title=videotomp3(url)
    filename=filename.replace("webm","mp3")
    scheduler.add_job(delete_file, 'date', args=[filename, 600])
    return send_file(filename[7:],as_attachment=True,download_name=video_title)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000)
