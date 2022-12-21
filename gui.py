from tkinter import *
from tkinter import ttk
from backend2 import *
from bs4 import BeautifulSoup as bs
import tkinter as tk




gui=Tk()

gui.title("SYNAPSE")
gui.geometry("900x400")
gui.config(bg="lightcyan")
top_frame=Frame(gui,bg="white",height="200",width="400")
top_frame.pack(pady=25)
outframe=Frame(gui,bg="pink")
outframe.pack(anchor="center")
my_input=Text(top_frame,height=1.5,width=80)
my_input.grid(row=0,column=1,padx=20,pady=50)

#function for dropdown
def dropdown():
    newvar=clicked.get()
    return newvar
#function for saving input
def saveinput():
   url=my_input.get(1.0,"end-1c")
   auth=tab2.get(1.0,"end-1c")
   head=tab3.get(1.0,"end-1c")
   drop=dropdown()
   code,text,header=request(drop,url,auth,head)
   soup=bs(text,'html.parser')
   prettyHtml=soup.prettify()
   lb1.insert(tk.END,prettyHtml)
   status.config(text="Status code :" + str(code))
   lb2.set_html(text)

def saveproject():
    link=my_input.get(1.0,"end-1c")
    
    
    

btn=Button(top_frame,text="send",command=saveinput)
btn.grid(row=0,column=2,padx=10)
btn=Button(top_frame,text="save")
btn.grid(row=0,column=3,padx=5)

option={
    "GET","PUT","POST","PATCH","DELETE"
}
clicked=StringVar()
clicked.set("GET")#for toplayer
drop=OptionMenu(top_frame,clicked,*option,command=dropdown)
drop.grid(row=0,column=0,padx=20)
drop.config(bg="red",fg="white",padx=20,pady=20,height=1,width=1)

#notebook
tabcontrol=ttk.Notebook(top_frame,height=100,width=800)
tab1=Text(tabcontrol,width=400)
tab2=Text(tabcontrol,width=400)
tab3=Text(tabcontrol,width=400)
tab4=Text(tabcontrol,width=400)
tabcontrol.add(tab1,text="Params")
tabcontrol.add(tab2,text="Authorization")
tabcontrol.add(tab3,text="Headers")
tabcontrol.add(tab4,text="JSON")
tabcontrol.grid(row=1,column=1,padx=10,pady=45)

#response area
responseframe=Frame(outframe,borderwidth=0,bg="#fff")
responseframe.pack()
sframe=Frame(responseframe,padx=3,bg="#fff",highlightbackground="black")
sframe.pack()
statusframe=Frame(sframe,bg="#fff")
statusframe.pack()

#statuscode creation
status=Label(statusframe,text="Status Code : 000",height=1,width=16)
status.pack()




#tabs output
tabcontrol=ttk.Notebook(responseframe,height=700,width=1200)
tab_1=Label(tabcontrol,text="",bg="#fff")
tab_2=Label(tabcontrol,text="",bg="#fff")
tab_3=Label(tabcontrol,text="",bg="#fff")

tabcontrol.add(tab_1,text="Raw")
tabcontrol.add(tab_2,text="Preview")
tabcontrol.add(tab_3,text="Headers")
tabcontrol.pack(fill="both")

#label creation
lb1= Text(tab_1,height=1150,width=100,padx=50,pady=50,bg="#fff")
lb1.pack()
lb2=Text(tab_2,height=1150,width=100,padx=50,pady=50,bg="#fff")
lb2.pack()
lb3= Label(tab_3,height=1150,width=100,padx=50,pady=50,bg="#fff")
lb3.pack()
          



gui.mainloop()
