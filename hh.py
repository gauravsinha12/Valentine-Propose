import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
image_file = "willmeet.jpg"
image = Image.open(image_file)

image = image.resize((500, 1200))

photo = ImageTk.PhotoImage(image)
msg_list = ["Maan jao na yrr please","Ye last baar maan jaa","Hone waale chintu ka fees mai bhar dunga","Mai kabhi kabhi khana bhi bbana dunga aur kuch ?","kitne baar se bol raha hun yrr maan jao","gussa aara mereko ab", "Ye last Baar hai ab nhi maani to fir bhul jaa Gaurav kaun hai."]

def show_message_boxx(a):
    if tk.messagebox.askyesno("Proposal", a):
        tk.messagebox.showinfo("Proposal", "Thank you for saying yes! Jaldi Milte hai")
        label = tk.Label(root, image=photo)
        label.pack()
        root.title("Yehi Theek Photo hai apna")
        root.mainloop()
        tk.messagebox.showinfo("Proposal", "Bye Dear Good Night")
        exit()

def show_message_box():
    tk.messagebox.showwarning("Errorr", "You Have been Hacked? IF you want to save your system then Agree to me")
    if tk.messagebox.askyesno("Proposal", "Will you be My Valentine"):
        tk.messagebox.showinfo("Proposal", "Thank you for saying yes! Jaldi Milte hai")
    else:
        tk.messagebox.showerror("Errorr", "Last Mauka hai dekh lo.")
        while True:
            for i in msg_list:
                show_message_boxx(i)

                
show_message_box()