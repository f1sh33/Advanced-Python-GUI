import customtkinter

def init(parent, categories_len):
    parent.navigation_frame = customtkinter.CTkFrame(parent, corner_radius=0)
    parent.navigation_frame.grid(row=0, column=0, sticky="nsew")
    parent.navigation_frame.grid_rowconfigure(categories_len+1, weight=1)
    parent.navigation_frame_label = customtkinter.CTkLabel(parent.navigation_frame, text="  Hardware Store", image=parent.logo_image,
                                                            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
    parent.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)