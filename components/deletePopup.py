import customtkinter
from operations import remove

categories = ["CPU", "GPU", "PSU", "Ram", "Mainboards", "Fans", "Monitors", "SSD", "Peripherals"]

# 1. Create a popup window
# 2. Submit the data to the remove function
# 3. Reload the page (update the changes)

class DeleteConfirmWindow(customtkinter.CTkToplevel):
    def __init__(self, ancestor, name, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Delete Confirm")
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
        classmethod(root.reset_page(page_name))