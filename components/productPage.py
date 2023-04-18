import customtkinter
from PIL import Image
import os
from operations import read

from components.editPopup import EditWindow
from components.createPopup import CreateWindow
from components.deletePopup import DeleteConfirmWindow

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images")
plus_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "white_plus.png")), size=(12, 12))

categories = ["CPU", "GPU", "PSU", "Ram", "Mainboards", "Fans", "Monitors", "SSD", "Peripherals"]

class ButtonBox(customtkinter.CTkFrame):
    def __init__(self, parent, ancestor, name, data, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        button1 = customtkinter.CTkButton(self, text="Edit", width=10, height=8, command=(lambda: self.open_edit_window(ancestor=ancestor, name=name, data=data)))
        button2 = customtkinter.CTkButton(self, text="Delete", width=10, height=8, command=(lambda: self.open_delete_confirm_window(ancestor=ancestor, name=name, data=data)))
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
            price_col = customtkinter.CTkLabel(self, text=(str(data[i]['price']) + "$"))
            stock_col = customtkinter.CTkLabel(self, text=data[i]['stock'])
            desc_col = customtkinter.CTkLabel(self, text=data[i]['description'])
            actions_col = ButtonBox(self, ancestor=ancestor, name=name, data=data[i], fg_color="transparent", corner_radius=10)

            id_col.grid(row=row_count, column=0, padx=5, pady=5, sticky="nsew")
            name_col.grid(row=row_count, column=1, padx=5, pady=5, sticky="nsew")
            price_col.grid(row=row_count, column=2, padx=5, pady=5, sticky="nsew")
            stock_col.grid(row=row_count, column=3, padx=5, pady=5, sticky="nsew")
            desc_col.grid(row=row_count, column=4, padx=5, pady=5, sticky="nsew")
            actions_col.grid(row=row_count, column=5, sticky="nsew", padx=4, pady=4)

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

        self.internal = Table(self, ancestor=ancestor, name=name, fg_color="#212134", border_width=2)
        self.internal.grid(row=1, column=0, padx=40, pady=40,sticky="nsew")


class ProductFrame(customtkinter.CTkFrame):
    def __init__(self, master, name, **kwags):
        super().__init__(master, **kwags)
        """ self.corner_radius=0
        self.fg_color="blue" """
        self.grid_columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.add_button = customtkinter.CTkButton(self, text=" Add new item", width=30 , font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=plus_logo, compound="left", command=(lambda: self.open_create_window(ancestor=master, name=name)))
        self.add_button.grid(row=0, column=1, padx=40, pady=40, ipadx=10, ipady=3, sticky="e")
        self.label = customtkinter.CTkLabel(self, text=name, font=customtkinter.CTkFont(size=35, weight="bold"))
        self.label.grid(row=0, column=0, padx=40, pady=(20, 10), sticky="w")

        self.frame = Frame(master=self, ancestor=master, name=name, corner_radius=10, fg_color="transparent")
        self.frame.grid(row=1, column=0, sticky="nsew", columnspan=2, rowspan=2)
        
        self.create_window = None

    def open_create_window(self, ancestor, name):
        if self.create_window is None or not self.create_window.winfo_exists():
            self.create_window = CreateWindow(ancestor=ancestor, name=name)  # create window if its None or destroyed
        else:
            self.create_window.focus()


def create_page(parent, name):
    origin_frame = ProductFrame(parent, name, corner_radius=0, fg_color="#181826")
    return origin_frame