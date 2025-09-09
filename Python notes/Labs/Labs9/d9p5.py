import tkinter as tk

root = tk.Tk()
root.title("Task 5 - Popup Menu")

text = tk.Text(root, width=50, height=10, wrap="word", undo=True)
text.pack(pady=8, fill="both", expand=True)
text.insert("1.0", "Try selecting some text, then right-click to Cut/Copy/Paste.")

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
menu.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
menu.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))

def show_menu(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()

text.bind("<Button-3>", show_menu)
text.bind("<Control-Button-1>", show_menu)

root.mainloop()
