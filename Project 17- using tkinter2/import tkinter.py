import tkinter
from tkinter import *
from tkinter import  messagebox


root=tkinter.Tk()
root.title("demo")
root.geometry("600x600")

#label
#label=tkinter.Label(root,text="Hiiii! I am Chandana. ").pack()
'''
#button #fg is font color . bg is background color ,
b=Button(root,text="Home love",bg="purple",fg="black")
b.grid(column=1,row=0)

#radio
r=Radiobutton(root,text="python",value=1)
r.grid(column=2,row=1)
r1=Radiobutton(root,text="c",value=1)
r1.grid(column=2,row=2)
r2=Radiobutton(root,text="c++",value=1)
r2.grid(column=2,row=3)

#entry
t=Entry(root,width=1000)
t.grid(column=3,row=0)'''

#message 
def Button1():
    messagebox.showinfo("status","Say I love you")
b=Button(root,text="chandana life",command=Button1)
b.pack()


    











root.mainloop()

