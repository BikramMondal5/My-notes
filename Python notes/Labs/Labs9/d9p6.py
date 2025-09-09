import tkinter as tk
from tkinter import ttk

def show_city():
    result.config(text=f"Selected: {cb.get()}")

root = tk.Tk()
root.title("Task 6 - Combobox")

ttk.Label(root, text="Select a city:").pack(anchor="w")
cities = ("Kolkata", "Mumbai", "Delhi", "Bengaluru", "Chennai")
cb = ttk.Combobox(root, values=cities, state="readonly", width=28)
cb.current(0)
cb.pack(pady=6)

result = ttk.Label(root, text="Selected city will appear here.")
result.pack(pady=10)

ttk.Button(root, text="Show Selected City", command=show_city).pack()

root.mainloop()
