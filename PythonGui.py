from tkinter import *

root = Tk()

root.title("Welcome my interface")
root.geometry('350x200')
lbl = Label(root, text= "My Page")
lbl.grid()

def clicked():
    btn['state'] = 'DISABLED'
    btn['text'] = 'Hello'
    btn['bg'] = 'white'
    lbl2 = Label(root,"Thank you!!!")
    lbl2.grid()

btn = Button(root,text="Hello:)",fg="white",bg="red",command=clicked)
btn.grid(column=1,row=0)
root.mainloop()