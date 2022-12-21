from tkinter import * #to make GUI
from tkinter import ttk #to create Tabs
import tkinter as tk #to use insert()
from backend import * #to connect frontend and backend
from bs4 import BeautifulSoup as bs #to arrange header
from pywebcopy import save_website #to make Save button functional
from tkhtmlview import HTMLLabel #for preview
from tkinter import messagebox #to make a message box


gui=Tk()
#window creation
gui.title("SYNAPSE")
gui.geometry("900x400")
gui.configure(bg="lightcyan")


#frame creation
top_frame=Frame(gui,bg="light green",width=900,height=50)
top_frame.pack(pady=20)

#output frame creation
output_frame=Frame(gui,bg="pink",width=900,height=200)
output_frame.pack(anchor="center",pady=10)

#Output label-My output is here
#output=Label(output_frame,text="My Output is here",height=2,bg="white")
#output.pack(padx=200,pady=100)

#input box creation
my_input=Text(top_frame,width=80,height=3,font="Canadara")
#my_input.configure(font=Font_tuple)
#my_input.pack(anchor="center",padx="45",pady="50")
my_input.grid(row=0,column=1,padx=20,pady=30)

#function
#DROPDOWN COMMAND
def dropdown(a):
    newvar=clicked.get()
    return (newvar)

#TO SAVE INPUT
def saveInput():
    url=my_input.get(1.0,"end-1c")
    param=tab1.get(1.0,"end-1c")
    auth=tab2.get(1.0,"end-1c")
    head=tab3.get(1.0,"end-1c")
    json=tab4.get(1.0,"end-1c")
    a=1
    drop=dropdown(a)
    code,text,header=request(drop,url,param,auth,head,json)
    soup=bs(text,'html.parser')
    prettyHTML=soup.prettify()
    lbl1.delete("1.0","end-1c")
    lbl1.insert(tk.END, prettyHTML)
    lbl2.set_html(text)
    status.config(text="Status Code: "+ str(code))
    lbl3.config(text=header)

def saveProject():
    link=my_input.get(1.0,"end-1c")
    save_website(url=link,project_folder="./saved_folder/")
    messagebox.showinfo("Success!","Project folder saved")

#button creation
btn1=Button(top_frame,text="Send",command=saveInput,font="Calibri")
btn1.grid(row=0,column=2,padx=10)

#button creation
btn2=Button(top_frame,text="Save",command=saveProject,font="Calibri")
btn2.grid(row=0,column=3,padx=10)

#DROPDOWN
option=["GET","PUT","POST","PATCH","DELETE"]
clicked=StringVar()
clicked.set("GET")
drop=OptionMenu(top_frame,clicked,*option,command=dropdown)
drop.grid(row=0,column=0,padx=20,pady=20)
drop.config(bg="light blue",padx=12,pady=12,font="Candara")

#TABS OF INPUT
tabControl= ttk.Notebook(output_frame,height=100,width=1500)
tab1=Text(tabControl,width=100,font="Canadara")
tab2=Text(tabControl,width=100,font="Canadara")
tab3=Text(tabControl,width=100,font="Canadara")
tab4=Text(tabControl,width=100,font="Canadara")
tabControl.add(tab1,text="PARAMS")
tabControl.add(tab2,text="Authorization")
tabControl.add(tab3,text="Headers")
tabControl.add(tab4,text="JSON")
tabControl.pack(fill="both")

#RESPONSE FOR INPUT
response_frame=Frame(gui,bg='#fff')
response_frame.pack()
sframe=Frame(response_frame,width=20,height=20,padx=3,pady=3,bg="#fff",highlightbackground="black",highlightthickness=5)
sframe.pack()
statusFrame=Frame(sframe,bg='#fff',width=15,height=10)
statusFrame.pack()

#TABS FOR PRINTING RESPONSE
tabControl=ttk.Notebook(response_frame,height=400,width=1200)
tab_1=Label(tabControl)
tab_2=Label(tabControl)
tab_3=Label(tabControl)
tabControl.add(tab_1,text="Raw")
tabControl.add(tab_2,text="Preview")
tabControl.add(tab_3,text="Headers")
tabControl.pack(fill="both")

lbl1=Text(tab_1,bg="#fff",font="Canadara")
lbl1.pack()
lbl2=HTMLLabel(tab_2,html="preview",bg="#fff",font="Canadara")
lbl2.pack()
lbl3=Label(tab_3,text="headers",bg="#fff",font="Canadara")
lbl3.pack()

#STATUS CODE
status=Label(statusFrame,text="Status Code:000",height=1,width=15,font="Candara")
status.pack()


gui.mainloop()