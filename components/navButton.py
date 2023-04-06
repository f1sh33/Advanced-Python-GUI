import customtkinter

def create_button(parent, name):
    return customtkinter.CTkButton(parent.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=name,
                                                   fg_color="transparent", text_color="#FFFFFF", hover_color="#181826", 
                                                   anchor="w", command=(lambda: highlight(parent, name)))

def test(parent):
    for attribute, value in parent.__dict__.items():
        print(attribute)

def highlight(parent, name):
    button_attribute_name = "nav_button_" + name
    page_attribute_name = "page_" + name
    for attribute, value in parent.__dict__.items():
        if "nav_button" in attribute:
            getattr(parent, attribute).configure(fg_color="transparent", text_color="#FFFFFF")
        if "page_" in attribute:
            getattr(parent, attribute).grid_forget()
    getattr(parent, button_attribute_name).configure(fg_color="#181826", text_color="#7977fc")
    getattr(parent, page_attribute_name).grid(row=0, column=1, sticky="nsew")