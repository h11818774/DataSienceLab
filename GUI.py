import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("600x400")




frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Vorhersage des Leasing Preises")
label.grid(row=0, column=1, columnspan=2, pady=12)

username_label = customtkinter.CTkLabel(master=frame, text="Marke:")
username_label.grid(row=1, column=0, padx=10, sticky="e")

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="auswählen...")
entry1.grid(row=2, column=0, padx=10, sticky="e")

password_label = customtkinter.CTkLabel(master=frame, text="Modell:")
password_label.grid(row=1, column=2, padx=10, sticky="e")

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="auswählen")
entry2.grid(row=2, column=2, padx=10, sticky="e")


root.mainloop()
