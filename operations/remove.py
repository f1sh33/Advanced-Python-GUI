import os
from operations import write
from operations import read

def remove(new_object):
    if os.path.getsize("db.json") <= 0:
        print("There is no database to remove.")
    else:
        control = read.read_all_data()
        id = new_object["id"]
        category_id = str(new_object["category_id"])
        del control[category_id][id]
        write.write_data(control)
