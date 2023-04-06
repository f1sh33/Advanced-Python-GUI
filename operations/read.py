import os
import json

def read_data(category_id):
    if os.path.getsize("db.json") > 0:
        with open("db.json", "r") as f:
            control = json.load(f)
            return control[category_id]
    else:
        print("The database is empty.")

def read_all_data():
    if os.path.getsize("db.json") > 0:
        with open("db.json", "r") as f:
            control = json.load(f)
            return control
    else:
        print("The database is empty.")