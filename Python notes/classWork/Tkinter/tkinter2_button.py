import tkinter as tk

# Create the main application window
root = tk.Tk()
# Create a button inside the root window
btn = tk.Button(root, text="Click Me", 
 bg="lightblue", fg="navy",
 width=15, height=2)
btn.pack(side="left")

btn1 = tk.Button(root, text="Hello", 
 bg="lightblue", fg="navy",
 width=15, height=2)
btn1.pack(side="left")

btn1.place(x=50, y=100, width=100, height=30)        

root.geometry("800x600")  # width=800, height=600
root.mainloop()