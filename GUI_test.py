import tkinter as tk
import customtkinter
import pandas as pd

df = pd.read_csv('data/preprocessed_df.csv') # csv file wird aus dem data folder geladen

def toggle_additional_options():
    if additional_options_checkbox_var.get():
        # Show the additional options labels
        horsepower_label.grid()
        entry9_horsepower.grid()
        kilowatts_label.grid()
        entry10_kilowatts.grid()
        fueltype_label.grid()
        fueltype_combobox4.grid()
    else:
        # Hide the additional options labels
        horsepower_label.grid_remove()
        entry9_horsepower.grid_remove()
        kilowatts_label.grid_remove()
        entry10_kilowatts.grid_remove()
        fueltype_label.grid_remove()
        fueltype_combobox4.grid_remove()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

additional_options_checkbox_var = customtkinter.BooleanVar(value=False)
additional_options_checkbox = customtkinter.CTkCheckBox(master=frame, text="Additional Options", variable=additional_options_checkbox_var, command=toggle_additional_options)
additional_options_checkbox.grid(row=8, column=1, pady=10)

# Label for Horsepower (initially hidden)
horsepower_label = customtkinter.CTkLabel(master=frame, text="Horsepower:")
entry9_horsepower = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")

# Label for Kilowatts (initially hidden)
kilowatts_label = customtkinter.CTkLabel(master=frame, text="Kilowatts:")
entry10_kilowatts = customtkinter.CTkEntry(master=frame, placeholder_text="fill out")

# Label for Fueltype (initially hidden)
fueltype_label = customtkinter.CTkLabel(master=frame, text="Fueltype:")
fueltype_combobox4 = customtkinter.CTkComboBox(master=frame, values=sorted(df["fuel_type"].unique().tolist()))

# Initially hide the additional options labels
horsepower_label.grid_remove()
entry9_horsepower.grid_remove()
kilowatts_label.grid_remove()
entry10_kilowatts.grid_remove()
fueltype_label.grid_remove()
fueltype_combobox4.grid_remove()

root.mainloop()
