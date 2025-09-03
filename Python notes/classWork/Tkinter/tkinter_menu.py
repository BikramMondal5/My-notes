import tkinter as tk
root = tk.Tk()
root.title("Menu Example")
# Create the main menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)
# Create File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: print("New file"))
file_menu.add_command(label="Open", command=lambda: print("Open file"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
# Create Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: print("Cut"))
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))
root.geometry("800x400")  # width=800, height=600
root.mainloop()
