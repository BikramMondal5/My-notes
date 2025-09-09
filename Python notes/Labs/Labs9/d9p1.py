# 1. Create a simple window with a label.

import tkinter as tk

root = tk.Tk()
root.title("Task 1 - Simple Label")

label = tk.Label(root, text="Hello, Tkinter! 👋")
label.pack(pady=20)

root.mainloop()
