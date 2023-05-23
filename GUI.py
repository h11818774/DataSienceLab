
import cmd
import customtkinter
import pandas as pd
import numpy as np

df = pd.read_csv('data/preprocessed_df.csv') # csv file wird aus dem data folder geladen


# Hier kann die Farbe von GUI eingestellt werden
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Das root Element ist das Element in dem alle weiteren Widgets eingebaut sind
root = customtkinter.CTk() # root element wird erstellt
root.geometry("800x600") # größe des root elements wird eingestellt
root.title("GUI Leasing Price") # Titel des Programms wird erstellt


# Im nächsten Bereich sind alle einzelnen Widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40, padx=80, fill="both", expand=True)
frame.place(in_=root, anchor="c", relx=.50, rely=.50) # frame wird in der mitte des feldes platziert

# Label für die Überschrift
label = customtkinter.CTkLabel(master=frame, text="Model for predicting leasing price", font=("TkDefaultFont", 12, "bold"))
label.grid(row=0, column=0, columnspan=3, padx=10, pady=12)

# Label für die Marke
marke_label = customtkinter.CTkLabel(master=frame, text="Brand:")
marke_label.grid(row=1, column=0, padx=10)

# Create the combobox for brand
marke_combobox1 = customtkinter.CTkComboBox(master=frame,
                                           values=sorted(df["brand_name"].unique().tolist()))
marke_combobox1.grid(row=2, column=0, padx=10)

# Label für das Modell
modell_label = customtkinter.CTkLabel(master=frame, text="Model:")
modell_label.grid(row=1, column=1, padx=10)

# Create the combobox for model
model_combobox2 = customtkinter.CTkComboBox(master=frame,
                                           values= sorted(df["model_name"].unique().tolist()))
model_combobox2.grid(row=2, column=1, padx=10)

# Label für die Kilometer
kilometer_label = customtkinter.CTkLabel(master=frame, text="Milage:")
kilometer_label.grid(row=3, column=0, padx=10)

# Eingabefeld für die Kilometer
entry3_kilometer = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")
entry3_kilometer.grid(row=4, column=0, padx=10)


# Label for First Registration
registration_label = customtkinter.CTkLabel(master=frame, text="First Registration:")
registration_label.grid(row=5, column=0, padx=10)

# Entryfield for First Registration
entry5_registration = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")
entry5_registration.grid(row=6, column=0, padx=10)


# Label for Contract Duration
duration_label = customtkinter.CTkLabel(master=frame, text="Contract Duration:")
duration_label.grid(row=5, column=1, padx=10)

# Entryfield for Contract Duration
entry6_duration = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")
entry6_duration.grid(row=6, column=1, padx=10)

def toggle_additional_options():
    if additional_options_checkbox_var.get():
        # Show the additional options labels
        gear_label.grid(row=8, column=0, padx=10)
        gear_combobox3.grid(row=9, column=0, padx=10)
        emission_label.grid(row=8, column=1, padx=10)
        entry7_emission.grid(row=9, column=1, padx=10)
        consumption_label.grid(row=10, column=0, padx=10)
        entry8_consumption.grid(row=11, column=0, padx=10)
        horsepower_label.grid(row=10, column=1, padx=10)
        entry9_horsepower.grid(row=11, column=1, padx=10)
        kilowatts_label.grid(row=12, column=0, padx=10)
        entry10_kilowatts.grid(row=13, column=0, padx=10)
        fueltype_label.grid(row=12, column=1, padx=10)
        fueltype_combobox4.grid(row=13, column=1, padx=10)

    else:
        # Hide the additional options labels
        gear_label.grid_remove()
        gear_combobox3.grid_remove()
        emission_label.grid_remove()
        entry7_emission.grid_remove()
        consumption_label.grid_remove()
        entry8_consumption.grid_remove()
        horsepower_label.grid_remove()
        entry9_horsepower.grid_remove()
        kilowatts_label.grid_remove()
        entry10_kilowatts.grid_remove()
        fueltype_label.grid_remove()
        fueltype_combobox4.grid_remove()

additional_options_checkbox_var = customtkinter.BooleanVar(value=False)
additional_options_checkbox = customtkinter.CTkCheckBox(master=frame, text="Additional Options", variable=additional_options_checkbox_var, command=toggle_additional_options)
additional_options_checkbox.grid(row=7, column=0, pady=10)

# Label for Gear
gear_label = customtkinter.CTkLabel(master=frame, text="Gear:")
gear_label.grid(row=8, column=0, padx=10)

# Entryfield for Gear - Create the combobox (dropdown menu) for brand
gear_combobox3 = customtkinter.CTkComboBox(master=frame,
                                           values= sorted(df["gear"].unique().tolist()))
gear_combobox3.grid(row=9, column=0, padx=10)

# Label for emission value
emission_label = customtkinter.CTkLabel(master=frame, text="Emission Value:")
emission_label.grid(row=8, column=1, padx=10)

# Entryfield for emission value
entry7_emission = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")
entry7_emission.grid(row=9, column=1, padx=10)

# Label for Consumption
consumption_label = customtkinter.CTkLabel(master=frame, text="Consumption:")
consumption_label.grid(row=10, column=0, padx=10)

# Entryfield for Consumption
entry8_consumption = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")
entry8_consumption.grid(row=11, column=0, padx=10)

#Label for Horsepower
horsepower_label = customtkinter.CTkLabel(master=frame, text="Horsepower:")
horsepower_label.grid(row=10, column=1, padx=10)

# Entryfield for Horsepower
entry9_horsepower = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")
entry9_horsepower.grid(row=11, column=1, padx=10)

# Label for Kilowatts
kilowatts_label = customtkinter.CTkLabel(master=frame, text="Kilowatts:")
kilowatts_label.grid(row=12, column=0, padx=10)

# Entryfield for Kilowatts
entry10_kilowatts = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")
entry10_kilowatts.grid(row=13, column=0, padx=10)

# Label for Fueltype
fueltype_label = customtkinter.CTkLabel(master=frame, text="Fueltype:")
fueltype_label.grid(row=12, column=1, padx=10)

# Entryfield for Fueltype - Create the combobox (dropdown menu) for brand
fueltype_combobox4 = customtkinter.CTkComboBox(master=frame,
                                           values= sorted(df["fuel_type"].unique().tolist()))
fueltype_combobox4.grid(row=13, column=1, padx=10)


#Initially hide entries
gear_label.grid_remove()
gear_combobox3.grid_remove()
emission_label.grid_remove()
entry7_emission.grid_remove()
consumption_label.grid_remove()
entry8_consumption.grid_remove()
horsepower_label.grid_remove()
entry9_horsepower.grid_remove()
kilowatts_label.grid_remove()
entry10_kilowatts.grid_remove()
fueltype_label.grid_remove()
fueltype_combobox4.grid_remove()

entry_fields = [marke_combobox1, model_combobox2, entry3_kilometer, entry5_registration,
                  entry6_duration, gear_combobox3, entry7_emission,
                 entry8_consumption, entry9_horsepower, entry10_kilowatts, fueltype_combobox4]
columns = ["Brand", "Model", "Milage", "Registration", "Duration", 
           "Gear", "Emission", "Consumption", "Horsepower",
           "Kilowatts", "Fueltype"]

#Funktion für den Berechnen Button
def button():
    df_entries = pd.DataFrame(columns=columns)
    for num, a in enumerate(entry_fields):
        if len(a.get()) == 0:
            column_name = columns[num]
            df_entries.loc[0, column_name] = np.nan
        else:
            column_name = columns[num]
            df_entries.loc[0, column_name] = a.get()



    # Filter the rows where the column "brand_name_Mazda" is equal to 1
    brand_monthly_fees = df.loc[df['brand_name'] == marke_combobox1.get(), 'monthly_fee'].mean()

    mylabel1 = customtkinter.CTkLabel(master=frame, text="Leasing Preis of " + marke_combobox1.get() + " will be calculated!")
    mylabel1.grid(row=15, column=0, columnspan=2)
    mylabel2 = customtkinter.CTkLabel(master=frame, text="Monthly Leasing Price: " + str(round(brand_monthly_fees)) + "€", font=("TkDefaultFont", 12, "bold")) # im moment wird einfach noch der erste eintrag vom Preis genommen -> mit modellen verknüpfen
    mylabel2.grid(row=16, column=0, columnspan=2)


    

#Code um den Berechnen Button zu erstellen
Button_calculate = customtkinter.CTkButton(master=frame, text="Calculate", command=button)
Button_calculate.grid(row=14, column=0, columnspan=2, pady=10)


root.mainloop()
