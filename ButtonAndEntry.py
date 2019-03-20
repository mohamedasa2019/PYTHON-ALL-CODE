from tkinter import *
from tkinter import ttk
root=Tk()

entry1=ttk.Entry(root,width=40)
entry1.pack()


bu1=ttk.Button(root,text="get text")
bu1.pack()

def buclick():
    print(entry1.get())
    entry1.delete(0,END)

bu1.config(command=buclick)







root.mainloop()