import customtkinter
from initialize import navButtonInit
from initialize import productPageInit
from initialize import imageInit
from initialize import navFrameInit
from initialize import windowInit

from components.productPage import ProductFrame

customtkinter.set_default_color_theme("theme.json")
categories = ["CPU", "GPU", "PSU", "Ram", "Mainboards", "Fans", "Monitors", "SSD", "Peripherals"]

# 1. Init windows and images
# 2. Grid navFrame to the left (row 0 column 0)
# 3. Grid navButtons to navFrame
# 4. Grid productPages to the right (row 0 column 1)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        windowInit.init(self)
        imageInit.init(self)
        navFrameInit.init(self, len(categories))
        navButtonInit.init(self, categories)
        productPageInit.init(self, categories)
    
    def reset_page(self, page_name):
        oldpage = getattr(self, page_name)
        oldpage.grid_forget()
        setattr(self, page_name, ProductFrame(self, page_name.split("_")[1], corner_radius=0, fg_color="#181826"))
        getattr(self, page_name).grid(row=0, column=1, sticky="nsew")
        oldpage.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

