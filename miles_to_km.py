import tkinter as tk
from tkinter import messagebox
from converter import miles_to_km

# This function is called when the button is clicked
def convert_and_display():
    user_input = input_box.get()
    try:
        km = miles_to_km(user_input)
        result_label.config(text=f"{km} kilometers")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")

# Create the main window
window = tk.Tk()
window.title("Miles to Kilometers")

# Create an entry box where the user can type in miles
input_box = tk.Entry(window)
input_box.pack(pady=5)

# Create a button that will call the convert function
convert_button = tk.Button(window, text="Convert", command=convert_miles_to_km)
convert_button.pack(pady=5)

# Create a label to show the result
result_label = tk.Label(window, text="")
result_label.pack(pady=5)

# Start the program (this keeps the window open)
window.mainloop()
