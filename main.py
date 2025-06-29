from tkinter import *
import socket 
from tkinter import filedialog
from tkinter import messagebox
import os

root=Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.config(bg="#f4fdfe")
root.resizable(False,False)

#icon
image_icon = PhotoImage(file="image/icon.png")
root.iconphoto(False, image_icon)

Label(root,text="File Transfer",font=("Acumin Variable Concept",20,"bold"),bg="#f4fdfe").place(x=20,y=30)

root.mainloop()
