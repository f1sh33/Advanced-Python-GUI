import customtkinter
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images")
plus_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "black_plus.jpg")), size=(12, 12))

def create_page(parent, name):
    origin_frame = customtkinter.CTkFrame(parent, corner_radius=0, fg_color="transparent")
    origin_frame.grid_columnconfigure(0, weight=1)
    add_button = customtkinter.CTkButton(origin_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=plus_logo, compound="left")
    label = customtkinter.CTkLabel(origin_frame, text=name, font=customtkinter.CTkFont(size=35, weight="bold"))
    add_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
    label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
    return origin_frame