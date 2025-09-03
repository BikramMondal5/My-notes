import tkinter as tk
from PIL import Image, ImageTk # For JPEG support

root = tk.Tk()
root.title("Image Display")
# Method 1: Native Tkinter (GIF/PNG only)
photo1 = tk.PhotoImage(file="logo.png")
label1 = tk.Label(root, image=photo1)
label1.image = photo1 # Keep a reference!
label1.pack()
# Method 2: Using Pillow (for JPEG and other formats)
pil_img = Image.open("photo.jpeg")
photo2 = ImageTk.PhotoImage(pil_img)
label2 = tk.Label(root, image=photo2)
label2.image = photo2 # Keep a reference!
label2.pack()
# Images on Canvas
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
canvas_img = canvas.create_image(200, 150, image=photo1)
root.mainloop() 
