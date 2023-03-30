import customtkinter
from initialize import navButtonInit
from initialize import productPageInit
from initialize import imageInit

categories = ["CPU", "GPU", "PSU", "Ram", "Mainboards", "Fans", "Monitors", "SSD", "Peripherals"]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hardware Management Software")
        self.geometry(f"{1280}x{700}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        imageInit.init(self)
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(len(categories)+1, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Hardware Store", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        navButtonInit.init(self, categories)
        productPageInit.init(self, categories)



if __name__ == "__main__":
    app = App()
    app.mainloop()

