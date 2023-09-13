import pandas
import os
import re

pattern = r'(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2}-\d{2})'

def extract_date(record):
    for record in os.listdir("data"):
        match = re.search(pattern, record)
        if match:
            date = match.group(1)
            return date
        else: return ""

def sort_files():
    files=os.listdir("data")
    return sorted(files,key=extract_date)

sorted_files=sort_files()
print(sorted_files)

