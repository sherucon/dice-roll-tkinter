import random
from tkinter import *
from tkinter import ttk

#def itCount(*args):
    #j=int(i.get())
    #j+=1
    #i.set(str(j))

def diceRoll(*args):
    val.set(str(random.randint(1,6)))
    #itCount()    

root=Tk()
root.title("Dice Roller")

mainframe=ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
root.columnconfigure(0)
root.rowconfigure(0)

#i=StringVar()
#i.set("0")
#ttk.Label(textvariable=i,width=5, anchor=CENTER).grid(column=1,row=0,sticky=(W,E))

val=StringVar()
ttk.Label(textvariable=val, width=5, anchor=CENTER).grid(column=0,row=0,sticky=(W,E))

b=ttk.Button(text="Roll!!!", command=diceRoll)
b.grid(column=0,row=1,sticky=(W,E))

root.bind("<Return>", lambda event: diceRoll())

for widget in root.winfo_children():
    widget.grid_configure(padx=3,pady=3)

root.mainloop()