import os
import random
from operations import read
from operations import write

def create_data(new_object):
    if os.path.getsize("db.json") > 0:
        control = read.read_all_data()
    else:
        control = {}
    check_id = []
    for i in control:
        for j in control[i]:
            check_id.append(j)
    category_id = new_object["category_id"]
    name = new_object["name"]
    price = new_object["price"]
    stock = new_object["stock"]
    description = new_object["description"]
    if int(category_id) <= 0 or int(category_id) > 9:
        print("Category is not found. Please try again.")
    elif price <= 0:
        print("Product price is not valid. Please try again.")
    elif stock < 0:
        print("Product quantity is not valid. Please try again.")
    elif description == 0:
        print("You must add description for the product.")
    else:
        if str(category_id) not in control:
            control[category_id] = {}
        while True:
            id = random.randint(100000, 999999)
            if str(id) not in check_id:
                break
        id = str(id)
        control[category_id][id] = {}
        control[category_id][id]["category_id"] = category_id
        control[category_id][id]["id"] = id
        control[category_id][id]["name"] = name
        control[category_id][id]["price"] = price
        control[category_id][id]["stock"] = stock
        control[category_id][id]["description"] = description
        write.write_data(control)
        