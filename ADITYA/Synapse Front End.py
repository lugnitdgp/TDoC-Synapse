import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk

frame = Tk()
frame.title("SYNAPSE")
frame.geometry("1260x820")
frame.config(bg='#fff')

fr1 = Frame(frame, borderwidth=0, bg= "linen", relief = SUNKEN, pady=40)
fr1.pack(fill= "x")
fr2 = Frame(fr1, borderwidth=0, bg= "linen", width=1000, pady=30)
fr2.pack(anchor= "center")

inputbox = Text(fr2, height=1, width=76, pady=20, padx= 20)
inputbox.grid(row=0, column=1, padx=45)

def Click():
    status = Label(statusframe, text= "Hello", height=1, width=16)
    status.pack()

sendButton = Button(fr2, text="Send", padx= 18, pady=15, bg = "#1338be", fg = "#fff")
sendButton.grid(row=0, column=2)
sendButton = Button(fr2, text="Save", padx= 18, pady=15, bg = "#1338be", fg = "#fff")
sendButton.grid(row=0, column=4)

#dropdown
def dropdown():
    newvar = clicked.get()
    print(newvar)

def saveinput():
    var = inputtxt.get(1.0, "end-1c")
    param = tab1.get(1.0, "end-1c")
    print(var)
    print(param)


option = [
    "GET",
    "PUT",
    "POST",
    "PATCH",
    "DELETE"
]

#data type of Menu Text()
clicked = StringVar()

# initial menu text
clicked.set("GET")

# dropdown menu
drop = OptionMenu(fr2, clicked, *option)
drop.grid(row=0, column=0)
drop.config(bg = "#1338be", fg = "#fff", padx = 20, pady=20)

# url box
inputtxt = Text(fr2, height=1, width=76, pady=20, padx=20)
inputtxt.grid(row = 0, column=1, padx=45)

# tabs widget
tabControl = ttk.Notebook(fr1, height=100, width=400)
tab1 = Text(tabControl, width=100)
tab2 = Text(tabControl, width=100)
tab3 = Text(tabControl, width=100)
tab4 = Text(tabControl, width=100)
tabControl.add(tab1, text='Params')
tabControl.add(tab2, text='Authorization')
tabControl.add(tab3, text='Headers')
tabControl.add(tab4, text='JSON')
tabControl.pack(fill="both", padx=40, pady=50)

responseframe = Frame(frame, borderwidth=0, bg="#fff")
responseframe.pack()
sframe = Frame(responseframe, padx=3, pady=3, bg="#fff", highlightbackground="black", highlightthickness=10)
sframe.pack()
statusframe = Frame(sframe, bg="#fff")
statusframe.pack()


tabControl= ttk.Notebook(responseframe, height = 700, width = 1200)
tab_1 = Label(tabControl, text="", bg="#fff")
tab_2 = Label(tabControl, text="", bg="#fff")
tab_3 = Label(tabControl, text="", bg="#fff")


tabControl.add(tab_1, text='Raw')
tabControl.add(tab_2, text='Preview')
tabControl.add(tab_3, text='Headers')

tabControl.pack(fill = "both")

status = Label(statusframe, text= "S")



frame.mainloop()




