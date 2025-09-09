import tkinter as tk

root = tk.Tk()
root.title("Task 4 - Canvas Shapes & Move")

canvas = tk.Canvas(root, width=400, height=260, bg="white")
canvas.pack(pady=10)

canvas.create_line(20, 20, 200, 20, width=2)
canvas.create_rectangle(20, 40, 120, 120, width=2)
circle_id = canvas.create_oval(250, 80, 310, 140, width=2, fill="")

def move(dx, dy):
    canvas.move(circle_id, dx, dy)

def on_key(event):
    if event.keysym == "Up":
        move(0, -10)
    elif event.keysym == "Down":
        move(0, 10)
    elif event.keysym == "Left":
        move(-10, 0)
    elif event.keysym == "Right":
        move(10, 0)

root.bind("<Up>", on_key)
root.bind("<Down>", on_key)
root.bind("<Left>", on_key)
root.bind("<Right>", on_key)

controls = tk.Frame(root)
controls.pack(pady=6)
tk.Button(controls, text="↑", width=3, command=lambda: move(0, -10)).grid(row=0, column=1)
tk.Button(controls, text="←", width=3, command=lambda: move(-10, 0)).grid(row=1, column=0)
tk.Button(controls, text="→", width=3, command=lambda: move(10, 0)).grid(row=1, column=2)
tk.Button(controls, text="↓", width=3, command=lambda: move(0, 10)).grid(row=2, column=1)

root.mainloop()
