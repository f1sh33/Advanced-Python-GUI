import customtkinter
from initialize import navButtonInit
from initialize import productPageInit
from initialize import imageInit
from initialize import navFrameInit
from initialize import windowInit

customtkinter.set_default_color_theme("theme.json")
categories = ["CPU", "GPU", "PSU", "Ram", "Mainboards", "Fans", "Monitors", "SSD", "Peripherals"]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        windowInit.init(self)
        imageInit.init(self)
        navFrameInit.init(self, len(categories))
        navButtonInit.init(self, categories)
        productPageInit.init(self, categories)


if __name__ == "__main__":
    app = App()
    app.mainloop()

