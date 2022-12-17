from tkinter import *
from tkinter import ttk
import tkinter as tk


#window creation
frame=Tk()
frame.title("Synapse")
frame.geometry("1260x820")
frame.config(bg='Lightcyan')

#frame creation
topframe=Frame(frame, bg="green", height='200', width='400')
topframe.pack(pady=25)

outputframe=Frame(frame,bg="pink")
outputframe.pack(anchor='center')

# #label
# output=Label(outputframe,bg="pink",text="my output is here", height=1)
# output.pack(padx=200,pady =40)

#inputbox
myinput=Text(topframe, height=1.5,width=80)
myinput.grid(row=0,column=1,padx=35,pady=50)


def click():
    status = Label(statusframe, text= "Hello", height=1, width=16)
    status.pack()

#buttom
sendButton = Button(topframe, text="Send",command=click, padx= 18, pady=15, bg = "#1338be", fg = "#fff")
sendButton.grid(row=0, column=2)
saveButton = Button(topframe, text="Save", padx= 18, pady=15, bg = "#1338be", fg = "#fff")
saveButton.grid(row=0, column=3)

#dropdown
def dropdown():
    newvar = clicked.get()
    print(newvar)

def saveinput():
    var = myinput.get(1.0, "end-1c")
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
drop = OptionMenu(topframe, clicked, *option)
drop.grid(row=0, column=0)
drop.config(bg = "#1338be", fg = "#fff", padx = 20, pady=20)


# tabs widget
tabControl = ttk.Notebook(outputframe, height=100, width=400)
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
sframe = Frame(responseframe, padx=3, pady=3, bg="#fff", highlightbackground="green", highlightthickness=3)
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