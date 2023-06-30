import customtkinter
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import os
from datetime import datetime
from dateutil import relativedelta


# #469DDD Zeb colour


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Wichtig: Numeric values müssen float sein, nicht int!
df = pd.read_csv('data/preprocessed.csv') # csv file wird aus dem data folder geladen


# Hier kann die Farbe von GUI eingestellt werden
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Das root Element ist das Element in dem alle weiteren Widgets eingebaut sind
root = customtkinter.CTk(fg_color="#469DDD") # root element wird erstellt
root.geometry("800x600") # größe des root elements wird eingestellt
root.title("GUI Leasing Price") # Titel des Programms wird erstellt

# Im nächsten Bereich sind alle einzelnen Widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40, padx=80, fill="both", expand=True)
frame.place(in_=root, anchor="c", relx=.50, rely=.50) # frame wird in der mitte des feldes platziert

# Label für die Überschrift
label = customtkinter.CTkLabel(master=frame, text="Leasing Price Predictor", font=("TkDefaultFont", 14, "bold"))
label.grid(row=0, column=0, columnspan=3, padx=10, pady=12)

# Label für die Marke
marke_label = customtkinter.CTkLabel(master=frame, text="Brand:")
marke_label.grid(row=1, column=0, padx=10)

values_brand = sorted(df["brand"].unique().tolist())
values_brand.append("Other")


# Create the combobox for brand

marke_combobox1 = customtkinter.CTkComboBox(master=frame,
                                           values=values_brand)

marke_combobox1.grid(row=2, column=0, columnspan=2, padx=10)
marke_combobox1.configure(width=300)


# Label für das Modell
modell_label = customtkinter.CTkLabel(master=frame, text="Model:")
modell_label.grid(row=3, column=0, padx=10)

values_model = sorted(df["model"].unique().tolist())
values_model.append("Other")

# Create the combobox for model
model_combobox2 = customtkinter.CTkComboBox(master=frame, values=values_model)
model_combobox2.grid(row=4, column=0, padx=10)


# Create the combobox for brand
def combobox_callback(choice):
    filtered_models = df.loc[df["brand"] == choice, "model"].unique().tolist()
    filtered_models.append("Other")
    model_combobox2.configure(values = filtered_models)

marke_combobox1 = customtkinter.CTkComboBox(master=frame,
                                           values=values_brand,
                                           command=combobox_callback)

marke_combobox1.grid(row=2, column=0, columnspan=2, padx=10)
marke_combobox1.configure(width=300)



# Label für die Kilometer
kilometer_label = customtkinter.CTkLabel(master=frame, text="Milage:")
kilometer_label.grid(row=3, column=1, padx=10)

# Eingabefeld für die Kilometer
entry3_kilometer = customtkinter.CTkEntry(master=frame, placeholder_text="in km")
entry3_kilometer.grid(row=4, column=1, padx=10)


# Label for First Registration
registration_label = customtkinter.CTkLabel(master=frame, text="First Registration:")
registration_label.grid(row=5, column=0, padx=10)

# Entryfield for First Registration
entry5_registration = customtkinter.CTkEntry(master=frame, placeholder_text="in months")
entry5_registration.grid(row=6, column=0, padx=10)
 



# Label for Contract Duration
duration_label = customtkinter.CTkLabel(master=frame, text="Contract Duration:")
duration_label.grid(row=5, column=1, padx=10)

# Entryfield for Contract Duration
entry6_duration = customtkinter.CTkEntry(master=frame, placeholder_text="in months")
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
        fueltype_label.grid(row=12, column=0, padx=10)
        fueltype_combobox4.grid(row=13, column=0, padx=10)

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
entry7_emission = customtkinter.CTkEntry(master=frame, placeholder_text="in g/km")
entry7_emission.grid(row=9, column=1, padx=10)

# Label for Consumption
consumption_label = customtkinter.CTkLabel(master=frame, text="Consumption:")
consumption_label.grid(row=10, column=0, padx=10)

# Entryfield for Consumption
entry8_consumption = customtkinter.CTkEntry(master=frame, placeholder_text="in l/100km")
entry8_consumption.grid(row=11, column=0, padx=10)

#Label for Horsepower
horsepower_label = customtkinter.CTkLabel(master=frame, text="Horsepower:")
horsepower_label.grid(row=10, column=1, padx=10)

# Entryfield for Horsepower
entry9_horsepower = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")
entry9_horsepower.grid(row=11, column=1, padx=10)

# Label for Fueltype
fueltype_label = customtkinter.CTkLabel(master=frame, text="Fueltype:")
fueltype_label.grid(row=12, column=0, padx=10)

# Entryfield for Fueltype - Create the combobox (dropdown menu) for brand
fueltype_combobox4 = customtkinter.CTkComboBox(master=frame,
                                           values= sorted(df["fuel"].unique().tolist()))
fueltype_combobox4.grid(row=13, column=0, padx=10)


#Initially hide entries
gear_label.grid_remove()
gear_combobox3.grid_remove()
emission_label.grid_remove()
entry7_emission.grid_remove()
consumption_label.grid_remove()
entry8_consumption.grid_remove()
horsepower_label.grid_remove()
entry9_horsepower.grid_remove()
fueltype_label.grid_remove()
fueltype_combobox4.grid_remove()


entry_fields = [marke_combobox1, model_combobox2, entry3_kilometer, entry5_registration,
                  entry6_duration, gear_combobox3, entry7_emission,
                 entry8_consumption, entry9_horsepower, fueltype_combobox4]
columns = ["brand", "model", "milage", "registration", "duration", 
           "gear", "emission", "consumption", "horsepower",
            "fuel"]

num_FEATURES = df[df.select_dtypes(include=['float64', 'int64']).columns].drop("fee", axis=1)
cat_FEATURES = df[df.select_dtypes(exclude=['float64', 'int64']).columns]
numeric_features = num_FEATURES.columns
categorical_features = cat_FEATURES.columns

column_names = list(numeric_features) + list(categorical_features)

mylabel1 = None
mylabel2 = None

#Funktion für den Berechnen Button
error_label = None  # Define the error_label as a global variable


def button():
    
    global error_label  # Add this line to access the global error_label variable

    if error_label is not None:
        error_label.destroy()
        error_label = None

    df_entries = pd.DataFrame(columns=columns)
    error_message = ""

    for num, a in enumerate(entry_fields):
        column_name = columns[num]
        value = a.get().strip()  # Remove leading/trailing whitespaces

        if column_name in ['brand', 'model', 'gear', 'fuel']:
            # Check if the field is one of the specified string fields
            if len(value) == 0:
                df_entries.loc[0, column_name] = np.nan
            else:
                df_entries.loc[0, column_name] = value
        else:
            # All other fields expect float values
            try:
                if len(value) > 0:
                    numeric_value = float(value)
                    if numeric_value.is_integer():
                        numeric_value = int(numeric_value)
                    df_entries.loc[0, column_name] = numeric_value
                else:
                    continue
            except ValueError:
                error_message += "Invalid input: " + column_name + "\n"
                break

    if len(error_message) > 0:
        # Show error message in GUI
        if error_label is not None:
            error_label.config(text=error_message)
        else:
            error_label = customtkinter.CTkLabel(master=frame, text=error_message, fg_color="#009FEO")
            error_label.grid(row=15, column=0, columnspan=2, pady=10)
            error_label.place


    df_X = df.drop('fee', axis=1)
    df_X = pd.concat([df_X, df_entries], axis=0, ignore_index=True)




    df_imputed = pd.DataFrame(df_X)#(preprocessor.fit_transform(df_X))

    entry_fields_imputet = df_imputed.tail(1)
    entry_fields_imputet.columns = column_names
    entry_fields_imputet = entry_fields_imputet[["registration", "milage", "duration", "emission", "consumption",
                                                "horsepower", "brand", "model", "gear", "fuel"]]
    entry_fields_imputet = entry_fields_imputet.rename(columns={'registration': 'registration',
                                                                'emission': 'emission',
                                                                'brand': 'brand',
                                                                'model': 'model',
                                                                'fuel': 'fuel'})
    print(entry_fields_imputet)

    # Clear the text when the button is pressed again
    global mylabel1, mylabel2
    if mylabel1 is not None:
        mylabel1.destroy()
    if mylabel2 is not None:
        mylabel2.destroy()

    # Model used
    loaded_model = joblib.load('models/current/randomForest.joblib')

    leasing_price = loaded_model.predict(entry_fields_imputet)
    print(leasing_price)

    mylabel2 = customtkinter.CTkLabel(master=frame, text="Monthly Leasing Price: " + str(round(leasing_price.item())) + "€", font=("TkDefaultFont", 14, "bold"))
    mylabel2.grid(row=16, column=0, columnspan=2)


#Code um den Berechnen Button zu erstellen
Button_calculate = customtkinter.CTkButton(master=frame, text="Calculate", command=button)
Button_calculate.grid(row=14, column=0, columnspan=2, pady=10)


root.mainloop()

