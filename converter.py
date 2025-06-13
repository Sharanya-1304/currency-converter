import tkinter as tk
from tkinter import ttk

# Hardcoded exchange rates (base: USD)
RATES = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.93,
    "GBP": 0.79,
    "JPY": 156.0
}

def convert():
    try:
        amount = float(entry_amount.get())
        from_curr = combo_from.get()
        to_curr = combo_to.get()
        usd_amount = amount / RATES[from_curr]
        result = round(usd_amount * RATES[to_curr], 2)
        label_result.config(text=f"{amount} {from_curr} = {result} {to_curr}")
    except:
        label_result.config(text="Invalid input!")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x300")
root.configure(bg="#f0f8ff")

tk.Label(root, text="Currency Converter", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=10)

tk.Label(root, text="Amount:", bg="#f0f8ff").pack()
entry_amount = tk.Entry(root, justify='center', font=("Arial", 12))
entry_amount.pack(pady=5)

tk.Label(root, text="From:", bg="#f0f8ff").pack()
combo_from = ttk.Combobox(root, values=list(RATES.keys()), state="readonly")
combo_from.set("USD")
combo_from.pack()

tk.Label(root, text="To:", bg="#f0f8ff").pack()
combo_to = ttk.Combobox(root, values=list(RATES.keys()), state="readonly")
combo_to.set("INR")
combo_to.pack()

tk.Button(root, text="Convert", command=convert, bg="#4682b4", fg="white", font=("Arial", 12)).pack(pady=10)
label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="green")
label_result.pack()

root.mainloop()