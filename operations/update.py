import os
from operations import write
from operations import read

def update_data(new_object):
    if os.path.getsize("db.json") <= 0:
        print("There is no database to update.")
    else:
        control = read.read_all_data()
        category_id = new_object["category_id"]
        id = new_object["id"]
        name = new_object["name"]
        price = new_object["price"]
        stock = new_object["stock"]
        description = new_object["description"]
        if int(category_id) <= 0 or int(category_id) > 9:
            print("Category is not found. Please try again.")
        elif category_id not in control:
            print("Could not find the specified product. Please try again.")
        elif id not in control[category_id]:
            print("ID of the product not found.")
        elif price <= 0:
            print("Product price is not valid. Please try again.")
        elif stock < 0:
            print("Product quantity is not valid. Please try again.")
        elif description == 0:
            print("You must add description for the product.")
        else:
            control[category_id][id]["category_id"] = category_id
            control[category_id][id]["id"] = id
            control[category_id][id]["name"] = name
            control[category_id][id]["price"] = price
            control[category_id][id]["stock"] = stock
            control[category_id][id]["description"] = description
            write.write_data(control)
            