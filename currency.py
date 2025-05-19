import tkinter as tk

# Static conversion rates (example)
rates = {
    "USD to INR": 83.2,
    "INR to USD": 1 / 83.2,
    "USD to EUR": 0.93,
    "EUR to USD": 1 / 0.93,
    "INR to EUR": 0.0112,
    "EUR to INR": 1 / 0.0112
}

def convert():
    try:
        amount = float(entry_amount.get())
        conversion = dropdown_var.get()
        rate = rates[conversion]
        result = round(amount * rate, 2)
        label_result.config(text=f"Result: {result}")
    except:
        label_result.config(text="Invalid input")

root = tk.Tk()
root.title("Currency Converter")

# Amount entry
tk.Label(root, text="Amount:", font=("Arial", 14)).grid(row=0, column=0, pady=10)
entry_amount = tk.Entry(root, font=("Arial", 14))
entry_amount.grid(row=0, column=1, pady=10)

# Dropdown for conversion type
tk.Label(root, text="Convert:", font=("Arial", 14)).grid(row=1, column=0)
dropdown_var = tk.StringVar(root)
dropdown_var.set("USD to INR")
dropdown = tk.OptionMenu(root, dropdown_var, *rates.keys())
dropdown.config(font=("Arial", 14))
dropdown.grid(row=1, column=1)

# Convert button
tk.Button(root, text="Convert", font=("Arial", 14), command=convert).grid(row=2, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 14))
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()
