from tkinter import *
from tkinter.ttk import *
from time import strftime
window = Tk()
window.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text = string)
    label.config(background="red")
    label.after(1000, time)

label = Label(window,font=("Arial Bold",50),background="black",foreground="pink")
label.grid(column=0,row=0)
time()
window.mainloop()



