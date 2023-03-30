from PIL import Image
import customtkinter
import os

def init(parent):
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images")
    parent.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
    parent.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
    parent.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
    parent.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
    parent.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
    parent.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                    dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))