import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

frame = tk.Frame(root, bg="lightblue", bd=2, relief="sunken")
frame.pack(padx=10, pady=10, fill="both", expand=True)

label = tk.Label(frame, text="I live inside a Frame")
label.pack(pady=20,side="left")

root.mainloop()
