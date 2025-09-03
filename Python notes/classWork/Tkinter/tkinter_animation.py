import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="black")
canvas.pack()

# Create a ball
ball = canvas.create_oval(10, 10, 30, 30, fill="#007EBD")
x_speed, y_speed = 4, 3  # Movement speed in pixels

def animate():
    # Get current ball position
    pos = canvas.coords(ball)
    print(pos)
    print()
    # Check for collisions with walls
    if pos[0] <= 0 or pos[2] >= 400:
        global x_speed
        x_speed = -x_speed
    if pos[1] <= 0 or pos[3] >= 300:
        global y_speed
        y_speed = -y_speed
    
    # Move the ball
    canvas.move(ball, x_speed, y_speed)
    
    # Schedule the next animation frame
    root.after(30, animate)  # 30ms = ~33 FPS

# Start animation
animate()

root.mainloop()
