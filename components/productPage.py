import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
import os
from operations import read
from operations import update
from operations import remove

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images")
plus_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "white_plus.png")), size=(12, 12))

categories = ["CPU", "GPU", "PSU", "Ram", "Mainboards", "Fans", "Monitors", "SSD", "Peripherals"]

class CreateWindow(customtkinter.CTkToplevel):
    def __init__(self, ancestor, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("470x400+%d+%d" % (1920/2 - 470/2, 1080/2 - 400/2))
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        var = tk.StringVar(value="HEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHE")

        label = customtkinter.CTkLabel(self, text="Create a product", height=50, font=customtkinter.CTkFont(size=20, weight="bold"))
        name_label = customtkinter.CTkLabel(self, text="Name", height=50)
        price_label = customtkinter.CTkLabel(self, text="Price", height=50)
        stock_label = customtkinter.CTkLabel(self, text="In stock", height=50)
        desc_label = customtkinter.CTkLabel(self, text="Description", height=50)

        cancel_button = customtkinter.CTkButton(self, text="Cancel", command=self.destroy)
        save_button = customtkinter.CTkButton(self, text="Save", command=(lambda: self.submit(name_input=name_input, price_input=price_input, stock_input=stock_input, desc_input=desc_input, ancestor=ancestor, name=name)))

        name_input = customtkinter.CTkEntry(self, width=300, height=30, corner_radius=10, placeholder_text="Enter Product's name...")
        price_input = customtkinter.CTkEntry(self, width=200, height=30, corner_radius=10, placeholder_text="Enter Product's price...")
        stock_input = customtkinter.CTkEntry(self, width=200, height=30, corner_radius=10, placeholder_text="Enter Product's stock number...")
        desc_input = customtkinter.CTkEntry(self, width=700, height=70, corner_radius=10, placeholder_text="Enter Product's description...", )
    

        label.grid(row=0, columnspan=2, sticky="w", padx=20)
        name_label.grid(row=1, columnspan=2, sticky="w", padx=20)
        name_input.grid(row=2, columnspan=2, sticky="w", padx=20)

        price_label.grid(row=3, column=0, padx=20, sticky="w")
        price_input.grid(row=4, column=0, padx=20, sticky="w")

        stock_label.grid(row=3, column=1, sticky="w")
        stock_input.grid(row=4, column=1, sticky="w")

        desc_label.grid(row=5, columnspan=2, sticky="w", padx=20)
        desc_input.grid(row=6, columnspan=2, sticky="w", padx=20)

        cancel_button.grid(row=7, column=0, sticky="nsew", padx=20, pady=20)
        save_button.grid(row=7, column=1, sticky="nsew", padx=20, pady=20)

    def submit(self, name_input, price_input, stock_input, desc_input, ancestor, name):
        prodcut_name = name_input.get()
        price = price_input.get()
        stock = stock_input.get()
        desc = desc_input.get()
        created_data = {
            "name": prodcut_name,
            "price": price,
            "stock": stock,
            "desc": desc
        }
        self.reset(ancestor, name)

    def reset(self, root, name):
        self.destroy()
        page_name = "page_" + name
        old_page = getattr(root, page_name)
        old_page.grid_forget()
        setattr(root, page_name, create_page(root, name))
        getattr(root, page_name).grid(row=0, column=1, sticky="nsew")
        old_page.destroy()

class EditWindow(customtkinter.CTkToplevel):
    def __init__(self, ancestor, name, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("470x400+%d+%d" % (1920/2 - 470/2, 1080/2 - 400/2))
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        old_name = tk.StringVar(value=data["name"])
        old_price = tk.StringVar(value=data["price"])
        old_stock = tk.StringVar(value=data["stock"])
        old_desc = tk.StringVar(value=data["description"])

        label = customtkinter.CTkLabel(self, text="Edit this product", height=50, font=customtkinter.CTkFont(size=20, weight="bold"))
        name_label = customtkinter.CTkLabel(self, text="Name", height=50)
        price_label = customtkinter.CTkLabel(self, text="Price", height=50)
        stock_label = customtkinter.CTkLabel(self, text="In stock", height=50)
        desc_label = customtkinter.CTkLabel(self, text="Description", height=50)

        cancel_button = customtkinter.CTkButton(self, text="Cancel", command=self.destroy)
        save_button = customtkinter.CTkButton(self, text="Save", command=(lambda: self.submit(name_input=name_input, price_input=price_input, stock_input=stock_input, desc_input=desc_input, ancestor=ancestor, name=name, data=data)))

        name_input = customtkinter.CTkEntry(self, width=300, height=30, corner_radius=10, placeholder_text="Enter Product's name...", textvariable=old_name)
        price_input = customtkinter.CTkEntry(self, width=200, height=30, corner_radius=10, placeholder_text="Enter Product's price...", textvariable=old_price)
        stock_input = customtkinter.CTkEntry(self, width=200, height=30, corner_radius=10, placeholder_text="Enter Product's stock number...", textvariable=old_stock)
        desc_input = customtkinter.CTkEntry(self, width=700, height=70, corner_radius=10, placeholder_text="Enter Product's description...", textvariable=old_desc )
    

        label.grid(row=0, columnspan=2, sticky="w", padx=20)
        name_label.grid(row=1, columnspan=2, sticky="w", padx=20)
        name_input.grid(row=2, columnspan=2, sticky="w", padx=20)

        price_label.grid(row=3, column=0, padx=20, sticky="w")
        price_input.grid(row=4, column=0, padx=20, sticky="w")

        stock_label.grid(row=3, column=1, sticky="w")
        stock_input.grid(row=4, column=1, sticky="w")

        desc_label.grid(row=5, columnspan=2, sticky="w", padx=20)
        desc_input.grid(row=6, columnspan=2, sticky="w", padx=20)

        cancel_button.grid(row=7, column=0, sticky="nsew", padx=20, pady=20)
        save_button.grid(row=7, column=1, sticky="nsew", padx=20, pady=20)

    def submit(self, name_input, price_input, stock_input, desc_input, ancestor, name, data):
        product_name = name_input.get()
        price = price_input.get()
        stock = stock_input.get()
        desc = desc_input.get()
        updated_data = {
            "name": product_name,
            "price": int(price),
            "stock": int(stock),
            "description": desc,
            "category_id": data["category_id"],
            "id": data["id"]
        }
        update.update_data(updated_data)
        self.reset(ancestor, name)

    def reset(self, root, name):
        self.destroy()
        page_name = "page_" + name
        old_page = getattr(root, page_name)
        old_page.grid_forget()
        setattr(root, page_name, create_page(root, name))
        getattr(root, page_name).grid(row=0, column=1, sticky="nsew")
        old_page.destroy()

class DeleteConfirmWindow(customtkinter.CTkToplevel):
    def __init__(self, ancestor, name, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x150+%d+%d" % (1920/2 - 200, 1080/2-75))
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        label = customtkinter.CTkLabel(self, text="Are you sure to delete this product?", height=50)
        button1 = customtkinter.CTkButton(self, text="No", command=self.destroy)
        button2 = customtkinter.CTkButton(self, text="Yes", command=(lambda: self.submit(id, ancestor, name)))
        label.grid(row=0, columnspan=2, sticky="nsew")
        button1.grid(row=1, column=0, ipadx=2)
        button2.grid(row=1, column=1, ipadx=2)
    
    def submit(self, id, ancestor, name):
        deleted_data = {
            "id": id,
            "category_id": categories.index(name) + 1,
        }
        remove.remove(deleted_data)
        self.reset(ancestor, name)

    def reset(self, root, name):
        self.destroy()
        page_name = "page_" + name
        old_page = getattr(root, page_name)
        old_page.grid_forget()
        setattr(root, page_name, create_page(root, name))
        getattr(root, page_name).grid(row=0, column=1, sticky="nsew")
        old_page.destroy()
        


class ButtonBox(customtkinter.CTkFrame):
    def __init__(self, parent, ancestor, name, data, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        button1 = customtkinter.CTkButton(self, text="Edit", width=2, height=2, command=(lambda: self.open_edit_window(ancestor=ancestor, name=name, data=data)))
        button2 = customtkinter.CTkButton(self, text="Delete", width=2, height=2, command=(lambda: self.open_delete_confirm_window(ancestor=ancestor, name=name, data=data)))
        button1.grid(row=0, column=0, ipadx=2)
        button2.grid(row=0, column=1, ipadx=2)
        self.delete_confirm = None
        self.edit_window = None

    def open_edit_window(self, ancestor, name, data):
        if self.edit_window is None or not self.edit_window.winfo_exists():
            self.edit_window = EditWindow(ancestor=ancestor, name=name, data=data)  # create window if its None or destroyed
        else:
            self.edit_window.focus()

    def open_delete_confirm_window(self, ancestor, name, data):
        if self.delete_confirm is None or not self.delete_confirm.winfo_exists():
            self.delete_confirm = DeleteConfirmWindow(id=data['id'], ancestor=ancestor, name=name)  # create window if its None or destroyed
        else:
            self.delete_confirm.focus()

class Table(customtkinter.CTkFrame):
    def __init__(self, parent, ancestor, name, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, **kwargs)
        headings = ["ID", "Name", "Price", "Stock", "Description", "Actions"]
        for i in range(6):
            label = customtkinter.CTkLabel(self, text=f"{headings[i]}", font=customtkinter.CTkFont(size=12, weight="bold"))
            label.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            if i == 4:
                self.grid_columnconfigure(i, weight=2)
            else:
                self.grid_columnconfigure(i, weight=1)
        data = read.read_data(str(categories.index(name) + 1))

        row_count = 1
        for i in data:
            id_col = customtkinter.CTkLabel(self, text=data[i]['id'])
            name_col = customtkinter.CTkLabel(self, text=data[i]['name'])
            price_col = customtkinter.CTkLabel(self, text=data[i]['price'])
            stock_col = customtkinter.CTkLabel(self, text=data[i]['stock'])
            desc_col = customtkinter.CTkLabel(self, text=data[i]['description'])
            actions_col = ButtonBox(self, ancestor=ancestor, name=name, data=data[i], fg_color="transparent")

            id_col.grid(row=row_count, column=0, padx=5, pady=5, sticky="nsew")
            name_col.grid(row=row_count, column=1, padx=5, pady=5, sticky="nsew")
            price_col.grid(row=row_count, column=2, padx=5, pady=5, sticky="nsew")
            stock_col.grid(row=row_count, column=3, padx=5, pady=5, sticky="nsew")
            desc_col.grid(row=row_count, column=4, padx=5, pady=5, sticky="nsew")
            actions_col.grid(row=row_count, column=5, sticky="nsew")

            self.grid_rowconfigure(row_count, weight=1)
            row_count += 1
        
        self.grid_rowconfigure(0, weight=0)

            


class Frame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, ancestor, name, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=0)
        self.grid_rowconfigure(index=1, weight=1)

        self.searchbar = customtkinter.CTkEntry(self, placeholder_text="Search", width=200, height=30)
        #self.searchbar.grid(row=0, column=0, sticky="w", padx=40)

        self.internal = Table(self, ancestor=ancestor, name=name, fg_color="transparent")
        self.internal.grid(row=1, column=0, padx=40, pady=40,sticky="nsew")


class ProductFrame(customtkinter.CTkFrame):
    def __init__(self, master, name, **kwags):
        super().__init__(master, **kwags)
        """ self.corner_radius=0
        self.fg_color="blue" """
        self.grid_columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.add_button = customtkinter.CTkButton(self, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=plus_logo, compound="left", command=(lambda: self.open_create_window(ancestor=master, name=name)))
        self.add_button.grid(row=0, column=1, padx=40, pady=40, sticky="e")
        self.label = customtkinter.CTkLabel(self, text=name, font=customtkinter.CTkFont(size=35, weight="bold"))
        self.label.grid(row=0, column=0, padx=40, pady=(20, 10), sticky="w")

        self.frame = Frame(master=self, ancestor=master, name=name, corner_radius=0, fg_color="transparent")
        self.frame.grid(row=1, column=0, sticky="nsew", columnspan=2, rowspan=2)
        
        self.create_window = None

    def open_create_window(self, ancestor, name):
        if self.create_window is None or not self.create_window.winfo_exists():
            self.create_window = CreateWindow(ancestor=ancestor, name=name)  # create window if its None or destroyed
        else:
            self.create_window.focus()


def create_page(parent, name):
    origin_frame = ProductFrame(parent, name, corner_radius=0, fg_color="transparent")
    return origin_frame