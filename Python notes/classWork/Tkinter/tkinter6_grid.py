import tkinter as tk

root = tk.Tk()
frame1 = tk.Frame(root,bg="lightblue")
frame1.pack(side="top", fill="x")


label1 = tk.Label(frame1,text='First Name').grid(row=0, column=0)
label2 = tk.Label(frame1,text='Last Name').grid(row=1, column=0)
e1 = tk.Entry(frame1)
e2 = tk.Entry(frame1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
root.geometry("400x300")

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    
frame2 = tk.Frame(root, bg="lightyellow")
frame2.pack(side="top", fill="both", expand=True)    
btn = tk.Button(frame2, text="Show Entry Fields", command=show_entry_fields,
 bg="lightblue", fg="navy",
 width=15, height=2)
btn.pack(pady=20)    
tk.mainloop()