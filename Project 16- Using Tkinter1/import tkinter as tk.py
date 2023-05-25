import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root=tk.Tk()
root.title("scrolltext")
root.geometry("900x900")
#label
ttk.Label(root,text="Python life is chandana",background="blue",foreground="white",font=("Times new Roman",15)).grid(row=0,column=1)

#scroll text
text1=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=40,height=10)
text1.grid(column=0,pady=10,padx=10)

text1.focus()


#combobox
'''n=tk.StringVar()
course=ttk.Combobox(root,width=27,textvariable=n)
course['values']=("python",
                  "django",
                  "machine learning")
course.grid(column=1,row=5)
course.current()'''
root.mainloop()



