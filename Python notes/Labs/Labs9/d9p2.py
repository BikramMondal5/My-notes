# A window with a button that updates a label when clicked

import tkinter as tk

def update_label():
    lbl.config(text="Label updated! ✅")

root = tk.Tk()
root.title("Task 2 - Update Label")

lbl = tk.Label(root, text="Click the button to update me", font=("Segoe UI", 12))
lbl.pack(pady=10)

btn = tk.Button(root, text="Update Label", command=update_label)
btn.pack(pady=10)

root.mainloop()

