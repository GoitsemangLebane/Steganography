# from fileinput import filename
from tkinter import *
from tkinter import messagebox
import customtkinter
import tkinter
from tkinter import filedialog
# import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

# colours dimensions  for GUI frame
customtkinter.set_appearance_mode('dark')

root_tk = tkinter.Tk()
root_tk.title("Steganography - Secret Writings")
root_tk.geometry("700x500+320+100")
root_tk.resizable(False, False)
root_tk.configure(bg="#2e2e2e", relief=FLAT)            # 2e2e2e/242424- color scheme for dark grey
root_tk.iconbitmap(r'logo1.ico')

button1 = PhotoImage(file="add image.png")
button2 = PhotoImage(file="save image.png")
button3 = PhotoImage(file="Hide data.png")
button4 = PhotoImage(file="Show data.png")

def insertImage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File',
                                          filetype=(("PNG file", "*.png"), ("JPG File", "*.jpg"), ("All file", "*.txt"))
                                          )
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img, width=250, height=250)
    lb1.image = img


def hide():
    message = text1.get(1.0, END)
    hidden = lsb.hide(str(filename), message)

    messagebox.showinfo("Confirmation", 'Data hidden successfully!')

def show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    message = text1.get(1.0, END)
    hidden = lsb.hide(str(filename), message)
    hidden.save("stash.png")
    messagebox.showinfo("Confirmation", 'Hidden message saved!')
    messagebox.showwarning('Closing Program', 'Session ending !')
    root_tk.destroy()

# open image

logo = Image.open("profilelogo.jpg")

# resize image
resized = logo.resize((75, 50), Image.LANCZOS)

new_logo = ImageTk.PhotoImage(resized)
logo = ImageTk.PhotoImage(file="profilelogo.jpg")
my_label = Label(root_tk, image=new_logo, bg="#2e2e2e")
my_label.place(x=20, y=15)

Label(root_tk, text="CYBER SCIENCE - THE FUTURE", bg='#2e2e2e', fg="white", font='kalinga 20 bold').place(x=170, y=20)

# first frame
frame1 = Frame(root_tk, bd=0, width=340, height=278, bg='black', relief=RAISED,)
frame1.place(x=10, y=80)
text_frame = Label(frame1, text="add image here...", font='kalinga 12 italic', fg='orange', bg='black')
text_frame.place(x=100, y=130)
lb1 = Label(frame1, bg='black')
lb1.place(x=40, y=10)


# second frame
frame2 = Frame(root_tk, bd=0, width=340, height=277, bg='brown', relief=FLAT)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="aerial 12", bg='white', fg='black', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=332, height=270)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=274)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# third frame
frame3 = Frame(root_tk, bd=0, bg='#2e2e2e', width=330, height=100, relief=FLAT)
frame3.place(x=10, y=370)

# config CTk Button

Button(frame3, image=button1, background='#2e2e2e', foreground='black', activebackground='white',
       activeforeground='white', command=insertImage, relief=FLAT).place(x=20, y=30)
Button(frame3, image=button2, background='#2e2e2e', foreground='black', activebackground='white',
       activeforeground='white', command=save, relief=FLAT).place(x=180, y=30)
Label(frame3, text='Picture, Image, Photo File', font='kalinga 10 bold', bg='#2e2e2e', fg='grey').place(x=20, y=5)

# fourth frame
frame4 = Frame(root_tk, bd=0, bg='#2e2e2e', width=330, height=100, relief=FLAT)
frame4.place(x=360, y=370)

Button(frame4, image=button3, background='#2e2e2e', foreground='black', activebackground='white',
       activeforeground='white', command=hide, relief=FLAT).place(x=20, y=30)
Button(frame4, image=button4, background='#2e2e2e', foreground='black', activebackground='white',
       activeforeground='white', command=show, relief=FLAT).place(x=180, y=30)
Label(frame4, text='hide your message in plain sight', font='kalinga 10 bold', bg='#2e2e2e', fg='grey').place(x=20, y=5)

root_tk.mainloop()
