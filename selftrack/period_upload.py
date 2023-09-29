import os

from decouple import config
from mega import Mega

mega = Mega()
email = config("EMAIL")
password = config("PASSWORD")
m = mega.login(email, password)

local_folder = "utils"
upload_url = "http://localhost:7000/importer"
text_file = "file_list.txt"

if not os.path.exists(text_file):
    open(text_file, "x")

current_list = open(text_file, "r").read().split("\n")
updated_list = []


def upload_file(record):
    print("[+] uploading file {record}")
    folder = m.find("selftrack")
    m.upload(record, folder[0])
    print("[+] upload complete")


def update_file_list():
    for root, _dirs, files in os.walk(local_folder):
        for record in files:
            current_record = f"{root}/{record}"
            if current_record not in current_list:
                updated_list.append(current_record)
                upload_file(current_record)
    with open(text_file, "a") as f:
        for record in updated_list:
            f.write(f"{record}\n")


update_file_list()
