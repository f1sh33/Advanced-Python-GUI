import json

def write_data(file_data):
    with open("db.json", "w") as f:
        json.dump(file_data, f, indent=4)