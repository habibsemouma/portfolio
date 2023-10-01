import os

from mega import Mega

email = os.environ.get("email")
password = os.environ.get("password")
mega = Mega()
m = mega.login(email, password)
current_files = os.listdir("data")


def importer():
    folder_node = m.find("selftrack")
    files = m.get_files_in_node(folder_node[0])
    for record in files:
        filename = files[record]["a"]["n"]
        if filename not in current_files:
            downloadable = m.find(filename)
            m.download(downloadable, "data")


importer()
