from components import navButton

def init(parent, categories):
    for index, category in  enumerate(categories):
        attr_name = "nav_button_" + category
        setattr(parent, attr_name, navButton.create_button(parent, category))
        getattr(parent, attr_name).grid(row=index+1, column=0, sticky="ew")