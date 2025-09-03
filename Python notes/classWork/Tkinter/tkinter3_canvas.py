import tkinter as tk

# Create the main application window
root = tk.Tk()

canvas = tk.Canvas(root, width=700, height=400)
canvas.pack()


line = None
rect = None
oval = None
# Draw shapes
def drawShapes():
    global line, rect, oval
    line = None
    rect = None
    oval = None    
    print("Draw Shapes")
    line = canvas.create_line(50, 50, 150, 150)
    rect = canvas.create_rectangle(150, 25, 200, 75, fill="blue")
    oval = canvas.create_oval(400, 50, 200, 100, fill="red")
    #root.geometry("600x300")  # width=800, height=600

# Change properties
def changeShapes():
    print("Change Shapes")
    global line, rect, oval
    if rect is not None:
        canvas.itemconfig(rect, fill="green")

    if oval is not None:
        # Move shapes
        canvas.move(oval, 10, 5)  # x and y offset

    if line is not None:
            #canvas.coords(line, 0, 0, 300, 300)  # new coordinates
        # Delete shapes
        canvas.delete(line)
          
btn = tk.Button(root, text="Draw Shapes", command=drawShapes,
 bg="lightblue", fg="navy",
 width=15, height=2)
btn.pack(pady=20)          

btn1 = tk.Button(root, text="Change Shape", command=changeShapes,
 bg="lightblue", fg="navy",
 width=15, height=2)
btn1.pack(pady=20) 


root.mainloop()