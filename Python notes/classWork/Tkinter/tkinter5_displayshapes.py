import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(padx=10, pady=10)
# Draw a rectangle
rect = canvas.create_rectangle(
50, 50, 150, 100, 
fill="#007EBD", 
outline="black", 
width=2
)
# Draw an oval
oval = canvas.create_oval(
200, 50, 300, 100, 
fill="yellow", 
outline="orange", 
width=2
)
# Draw a line
line = canvas.create_line(
50, 150, 300, 200, 
fill="red", 
width=3, 
arrow=tk.LAST
)
root.mainloop()
