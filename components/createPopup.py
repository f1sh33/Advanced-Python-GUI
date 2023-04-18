import customtkinter
from operations import create

categories = ["CPU", "GPU", "PSU", "Ram", "Mainboards", "Fans", "Monitors", "SSD", "Peripherals"]

class CreateWindow(customtkinter.CTkToplevel):
    def __init__(self, ancestor, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Create a new product")
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
            "price": int(price),
            "stock": int(stock),
            "description": desc,
            "category_id": str(categories.index(name) + 1)
        }
        create.create_data(created_data)
        self.reset(ancestor, name)

    def reset(self, root, name):
        self.destroy()
        page_name = "page_" + name
        classmethod(root.reset_page(page_name))