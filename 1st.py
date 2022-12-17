from tkinter import *
from tkinter import ttk
import tkinter as tk
gui= Tk()
gui.title("SYNAPSE")
gui.geometry("1024x400")
gui.config(bg="#ffffff")

top_frame=Frame(gui,borderwidth=0, bg="#ffd700",relief='sunken',pady=40,)
top_frame.pack(fill='x')
outputframe=Frame(top_frame,bg='#ffd700',borderwidth=0,pady=30)
outputframe.pack(anchor='center')

my_input = Text(outputframe,height=1,width=76,pady=20,padx=20)
my_input.grid(row=0, column=1,padx=45)

def saveinput():
    var=my_input.get(1.0,"end-1c")
    params=tab1.get(1.0,"end-1c")
    author=tab2.get(1.0,"end-1c")
    head=tab3.get(1.0,"end-1c")
    json1=tab4.get(1.0,"end-1c")
    tab_1.config(text=var)
    print(var)
    print(params)
    print(author)
    print(head)
    print(json1)


def dropdown(self):
    newvar=clicked.get()
    print(newvar)


sendbtn=Button(outputframe,text="send",bg='lavender',fg='black',padx=20,command=saveinput)
sendbtn.grid(row=0, column=2)
savebtn=Button(outputframe,text="save",bg='lavender',fg='black',padx=20)
savebtn.grid(row=0, column=4)

option=[
    "GET",
    "PUT",
    "POST",
    "PATCH",
    "DELETE"
]
clicked=StringVar()
clicked.set("GET")
drop= OptionMenu(outputframe,clicked,*option,command=dropdown)
drop.grid(row=0,column=0)
drop.configure(bg="lavender",fg="black",padx=20)

tabcontrol=ttk.Notebook(top_frame,height=100,width=400)
tab1=Text(tabcontrol,width=100)
tab2=Text(tabcontrol,width=100)
tab3=Text(tabcontrol,width=100)
tab4=Text(tabcontrol,width=100)
tabcontrol.add(tab1,text='params')
tabcontrol.add(tab2,text='authorization')
tabcontrol.add(tab3,text='headers')
tabcontrol.add(tab4,text='json')
tabcontrol.pack(fill='both',padx=40,pady=45)

#responseframe
responseframe=Frame(gui,borderwidth=0,bg='#fff')
responseframe.pack()
sframe=Frame(responseframe,padx=3,pady=3,bg='#fff',highlightbackground='black',highlightthickness=3)
sframe.pack()
statusframe=Frame(sframe,bg="#fff")
statusframe.pack()



#tab output
tabcontrol=ttk.Notebook(gui,height=700,width=1200)
tab_1=Label(tabcontrol,width=100,height=10,text="",bg='#fff')
tab_2=Label(tabcontrol,width=100,height=9,text="",bg='#fff')
tab_3=Label(tabcontrol,width=100,height=9,text="",bg='#fff')
tabcontrol.add(tab_1,text ='Raw')
tabcontrol.add(tab_2,text ='Preview')
tabcontrol.add(tab_3,text ='Headers')
tabcontrol.pack()


status=Label(statusframe,text="status code:000",height=1,width=16)
status.pack()
gui.mainloop()

