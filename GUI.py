
import customtkinter

# Hier kann die Farbe von GUI eingestellt werden
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Das root Element ist das Element in dem alle weiteren Widgets eingebaut sind
root = customtkinter.CTk()
root.geometry("600x400")



# Im nächsten Bereich sind alle einzelnen Widgets
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


#Funktion für den Berechnen Button
def button():
    mylabel = customtkinter.CTkLabel(master=frame, text="Leasing Preis wird berechnet!")
    mylabel.grid(row=6, column=1)

#Code um den Berechnen Button zu erstellen
Button_calculate = customtkinter.CTkButton(master=frame, text="Berechnen", command=button)
Button_calculate.grid(row=5, column=1)


root.mainloop()
