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

def Send():
    window = Toplevel(root)
    window.title("Send File")
    window.geometry("450x560+500+200")
    window.config(bg="#f4fdfe")
    window.resizable(False, False)

    #icoon
    image_icon1 = PhotoImage(file="image/send.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file= "image/sender.png")
    Label(window, image=Sbackground).place(x=-2, y=0)

    Mbackground = PhotoImage(file = "image/id.png")
    Label(window, image= Mbackground, bg="#f4fdfe").place(x=100, y=260)

    Button(window, text= "Select File", width = 10, height= 1, font=('ariel 14 bold'), bg="#fff", fg="#000").place(x=160, y=150)
    Button(window, text="SEND", width=8, height=1, font=('ariel 14 bold'), bg="#000", fg="#fff").place(x=300, y=150)

    window = mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive File")
    main.geometry("450x560+500+200")
    main.config(bg="#f4fdfe")
    main.resizable(False, False)

    #icoon
    image_icon1 = PhotoImage(file="image/receive.png")
    main.iconphoto(False, image_icon1)

    main = mainloop()

#icon
image_icon = PhotoImage(file="image/icon.png")
root.iconphoto(False, image_icon)

Label(root,text="File Transfer",font=("Acumin Variable Concept",20,"bold"),bg="#f4fdfe").place(x=20,y=30)

Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25,y=80)

send_image= PhotoImage(file="image/send.png")
send=Button(root, image=send_image,bg="#f4fdfe", bd=0, command = Send)
send.place(x=50,y=100)

receive_image= PhotoImage(file="image/receive.png")
receive=Button(root, image=receive_image,bg="#f4fdfe", bd=0, command = Receive)
receive.place(x=300,y=100)

Label(root, text="Send", font=("Acumin Variable Concept", 15, "bold"), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=("Acumin Variable Concept", 15, "bold"), bg="#f4fdfe").place(x=300, y=200)


background_image = PhotoImage(file="image/background.png")
Label(root, image=background_image).place(x=-2, y=323)


root.mainloop()
