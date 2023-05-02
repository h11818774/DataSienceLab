
import customtkinter
import pandas as pd

# Hier kann die Farbe von GUI eingestellt werden
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Das root Element ist das Element in dem alle weiteren Widgets eingebaut sind
root = customtkinter.CTk() # root element wird erstellt
root.geometry("600x400") # größe des root elements wird eingestellt
root.title("GUI Leasing Price") # Titel des Programms wird erstellt


# Im nächsten Bereich sind alle einzelnen Widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
frame.place(in_=root, anchor="c", relx=.50, rely=.30) # frame wird in der mitte des feldes platziert

# Label für die Überschrift
label = customtkinter.CTkLabel(master=frame, text="Vorhersage des Leasing Preises")
label.grid(row=0, column=0, columnspan=3, padx=10, pady=12)

# Label für die Marke
marke_label = customtkinter.CTkLabel(master=frame, text="Marke:")
marke_label.grid(row=1, column=0, padx=10)

# Eingabefeld für die Marke
entry1_marke = customtkinter.CTkEntry(master=frame, placeholder_text="auswählen...")
entry1_marke.grid(row=2, column=0, padx=10)

# Label für das Modell
modell_label = customtkinter.CTkLabel(master=frame, text="Modell:")
modell_label.grid(row=1, column=2, padx=10)

# Eingabefeld für das Modell
entry2_modell = customtkinter.CTkEntry(master=frame, placeholder_text="auswählen")
entry2_modell.grid(row=2, column=2, padx=10)

# Label für die Kilometer
kilometer_label = customtkinter.CTkLabel(master=frame, text="Kilometer:")
kilometer_label.grid(row=3, column=0, padx=10)

# Eingabefeld für die Kilometer
entry3_kilometer = customtkinter.CTkEntry(master=frame, placeholder_text="auswählen")
entry3_kilometer.grid(row=4, column=0, padx=10)

# Label für Deposit
deposit_label = customtkinter.CTkLabel(master=frame, text="Deposit:")
deposit_label.grid(row=3, column=2, padx=10)

# Eingabefeld für Deposit
entry4_deposit = customtkinter.CTkEntry(master=frame, placeholder_text="auswählen")
entry4_deposit.grid(row=4, column=2, padx=10)


#Funktion für den Berechnen Button
def button():
    df = pd.read_csv('data/preprocessed_df.csv') # csv file wird aus dem data folder geladen
    # Filter the rows where the column "brand_name_Mazda" is equal to 1
    brand_monthly_fees = df.loc[df['brand_name'] == entry1_marke.get(), 'monthly_fee'].mean()

    mylabel1 = customtkinter.CTkLabel(master=frame, text="Leasing Preis von " + entry1_marke.get() + " wird berechnet!")
    mylabel1.grid(row=6, column=1)
    mylabel2 = customtkinter.CTkLabel(master=frame, text="Monatlicher Leasing Preis: " + str(brand_monthly_fees)) # im moment wird einfach noch der erste eintrag vom Preis genommen -> mit modellen verknüpfen
    mylabel2.grid(row=7, column=1)

#Code um den Berechnen Button zu erstellen
Button_calculate = customtkinter.CTkButton(master=frame, text="Berechnen", command=button)
Button_calculate.grid(row=5, column=1)


root.mainloop()
