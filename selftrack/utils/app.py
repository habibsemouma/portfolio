from flask import Flask, jsonify,request
from flask_cors import CORS
from utils import *
from werkzeug.utils import secure_filename
import os
from mega import Mega
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import pandas
import json
import datetime

scheduler = BackgroundScheduler()

app = Flask(__name__)
CORS(app, origins='*')
app.config['UPLOAD_FOLDER'] = "./data"

email = os.environ.get("email")
password = os.environ.get("password")
mega=Mega()
m = mega.login(email, password)
current_files=os.listdir("data")

def importer():
    folder_node = m.find("selftrack")
    files = m.get_files_in_node(folder_node[0])
    for record in files:
        filename = files[record]['a']['n']
        if filename not in current_files:
            downloadable=m.find(filename)
            m.download(downloadable,"data")



