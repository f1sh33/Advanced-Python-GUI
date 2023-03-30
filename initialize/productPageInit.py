from components import productPage

def init(parent, categories):
    for index, category in  enumerate(categories):
        attr_name = "page_" + category
        setattr(parent, attr_name, productPage.create_page(parent, category))

    parent.page_CPU.grid(row=0, column=1, sticky="nsew")
    parent.page_GPU.grid(row=0, column=1, sticky="nsew")
    parent.page_CPU.grid_forget()