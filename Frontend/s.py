from tkinter import *
from tkinter import ttk
# import tkinter as tk
gui=Tk()
#gui logic

#window creation
gui.title("SYNAPSE")
gui.geometry("900x400")
gui.config(bg="cyan")

top_frame=Frame(gui,bg="white",height="200",width="400")
top_frame.pack(pady=25)

my_input=Text(top_frame, height=2, width=80)
# my_input.pack(anchor="center",padx=45,pady=50)
my_input.grid(row=0, column=1,padx=25,pady=90)

outputframe=Frame(gui,bg="pink")
outputframe.pack(anchor="center")

output=Label(outputframe, height=2,bg="pink", fg="red")
output.pack(padx=200,pady=40)

def Click():
   status=Label(statusframe,text="Status code:000",height=1,width=16)
   status.pack()

btn=Button(top_frame,text="Send",command=Click,height=2,width=10)
btn.grid(row=0,column=2,padx=25)

btn1=Button(top_frame,text="Save",height=2,width=10)
btn1.grid(row=0,column=3,padx=25)

option=[
    "GET",
    "PUT",
    "POST",
    "PATCH",
    "DELETE"
]
clicked=StringVar()
clicked.set("GET")
drop=OptionMenu(top_frame,clicked,*option)
drop.grid(row=0,column=0)
drop.config(padx=30,pady=40)

tabControl=ttk.Notebook(output,height=150,width=1000)
tab1=Text(tabControl,width=100)
tab2=Text(tabControl,width=100)
tab3=Text(tabControl,width=100)
tab4=Text(tabControl,width=100)
tabControl.add(tab1,text="Params")
tabControl.add(tab2,text="Authorization")
tabControl.add(tab3,text="Headers")
tabControl.add(tab4,text="JSON")
tabControl.pack(fill="both",padx=40,pady=45)

#response area
responseframe=Frame(gui,borderwidth=0,bg="#fff")
responseframe.pack()
sframe=Frame(responseframe,padx=3,pady=3,bg="#fff",highlightbackground="black",highlightthickness=3)
sframe.pack()
statusframe=Frame(sframe,bg="#fff")
statusframe.pack()

#tabs output
tabControl=ttk.Notebook(responseframe,height=700,width=1200)
tab_1=Label(tabControl,text="",bg="#fff")
tab_2=Label(tabControl,text="",bg="#fff")
tab_3=Label(tabControl,text="",bg="#fff")
tabControl.add(tab_1,text="Raw")
tabControl.add(tab_2,text="Preview")
tabControl.add(tab_3,text="Headers")
tabControl.pack(fill="both")

# status=Label(statusframe,text="Status code:000",height=1,width=16)
# status.pack()


gui.mainloop()