# Take input from the user and display it in a label below when clicked on the button

import tkinter as tk

def show_text():
    out.config(text=entry.get() if entry.get() else "(empty)")

root = tk.Tk()
root.title("Task 3 - Input → Label")

tk.Label(root, text="Enter something:").pack(anchor="w")
entry = tk.Entry(root, width=30)
entry.pack(pady=6, fill="x")

out = tk.Label(root, text="Your text will appear here ↓")
out.pack(pady=10)

tk.Button(root, text="Display Below", command=show_text).pack()

root.mainloop()
