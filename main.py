import tkinter as tk
import requests

# Set up the GUI window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.configure(bg="#1E1E1E")

# Set up the labels and entry fields for currency conversion
from_currency_label = tk.Label(root, text="From Currency:", fg="white", bg="#1E1E1E")
from_currency_label.grid(row=0, column=0, padx=10, pady=10)
from_currency_entry = tk.Entry(root, width=20)
from_currency_entry.grid(row=0, column=1, padx=10, pady=10)

to_currency_label = tk.Label(root, text="To Currency:", fg="white", bg="#1E1E1E")
to_currency_label.grid(row=1, column=0, padx=10, pady=10)
to_currency_entry = tk.Entry(root, width=20)
to_currency_entry.grid(row=1, column=1, padx=10, pady=10)

amount_label = tk.Label(root, text="Amount:", fg="white", bg="#1E1E1E")
amount_label.grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root, width=20)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="", fg="white", bg="#1E1E1E")
result_label.grid(row=4, column=1, padx=10, pady=10)

# Define the conversion function
def convert_currency():
    try:
        from_currency = from_currency_entry.get().upper()
        to_currency = to_currency_entry.get().upper()
        amount = float(amount_entry.get())

        # Make an API request to get the conversion rate
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        conversion_rate = data["rates"][to_currency]

        # Calculate the converted amount and display the result
        result = amount * conversion_rate
        result_label.config(text=f"{result:.2f} {to_currency}")
    except:
        result_label.config(text="Invalid input")

# Set up the button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert_currency, bg="#4F4F4F", fg="white")
convert_button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()