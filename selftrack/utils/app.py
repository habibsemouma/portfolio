import os
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask,jsonify
from flask_cors import CORS
from mega import Mega
from utils import *
import json

scheduler = BackgroundScheduler()

app = Flask(__name__)
CORS(app, origins="*")
app.config["UPLOAD_FOLDER"] = "./data"

email = os.environ.get("email")
password = os.environ.get("password")
current_files = os.listdir("data")


def importer():
    mega = Mega()
    m = mega.login(email, password)
    folder_node = m.find("selftrack")
    files = m.get_files_in_node(folder_node[0])
    for record in files:
        filename = files[record]["a"]["n"]
        if filename not in current_files:
            downloadable = m.find(filename)
            m.download(downloadable, "data")
