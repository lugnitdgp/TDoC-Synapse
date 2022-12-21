from tkinter import *
from tkinter import ttk
import tkinter as tk
from backend import *
from bs4 import BeautifulSoup as bs 
from pywebcopy import save_website
from tkhtmlview import HTMLLabel
from tkinter import messagebox

gui = Tk()

#window creation
gui.title("SYNAPSE")
gui.geometry("900x400")
gui.config(bg='white')

#frame creation
top_frame = Frame(gui, bg = "pink", height = "400", width = "100")
top_frame.pack()

#label
output_frame = Frame(gui, bg="yellow")
output_frame.pack(anchor="center")

output = Label(output_frame, text="My output is here", height=1, bg="yellow", fg="black")
output.pack(padx=100, pady=10)

#input box
my_input = Text(top_frame, height = 1.5, width = 80)
#my_input.pack(anchor="center", padx=45, pady=50)
my_input.grid(row=0, column=1, padx=35, pady=50)

#def Click():
 #   status = Label(statusframe, text="Hello", height=1, width=16)
  #  status.pack()

#function
#function for dropdown
def dropdown():
    newvar = clicked.get()
    print(newvar)
    return newvar
#function for saving the input
def saveinput():
    url = my_input.get(1.0, "end-1c")
    param = tab1.get(1.0, "end-1c") 
    auth = tab2.get(1.0, "end-1c")
    head = tab3.get(1.0, "end-1c")
    drop = dropdown()
    code, text, header = request(drop, url, auth, head)
    soup = bs(text, 'html.parser')
    prettyHTML = soup.prettify()

    lbl1.insert(tk.END, prettyHTML)
    lbl2.set_html(text)
    status.config(text="Status code:"+str(code))

def saveproject():
    link = my_input.get(1.0, "end-1c")
    save_website(url=link, project_folder = "./saved_folder/")
    messagebox.showinfo("Success!", "Project folder saved")

   
#button
sendbtn = Button(top_frame, text="Send", padx=20, pady=15, bg="white", fg="black", command=saveinput)
sendbtn.grid(row=0, column=2)

savebtn = Button(top_frame, text="Save", padx=20, pady=15, bg="white", fg="black", command=saveproject)
savebtn.grid(row=0, column=4)

#dropdown menu
option = [
    "GET",
    "PUT",
    "POST",
    "PATCH",
    "DELETE",
    
]
#datatype for menu text
clicked = StringVar()
#initial menu text
clicked.set("GET")
#creat dropdown menu
drop = OptionMenu(top_frame, clicked, *option, command=dropdown)
drop.grid(row=0, column=0)
drop.config(bg="white", fg="black", padx=20, pady=15)

#notebook
tabControl = ttk.Notebook(top_frame, height= 100, width= 1200)
tab1 = Text(tabControl, width= 100)
tab2 = Text(tabControl, width= 100)
tab3 = Text(tabControl, width= 100)
tab4 = Text(tabControl, width= 100)
tabControl.add(tab1, text='Params')
tabControl.add(tab2, text='Authorization')
tabControl.add(tab3, text='Headers')
tabControl.add(tab4, text='JSON')
tabControl.grid(row=1, column=1,  padx=40, pady=45)

#response area
responseframe = Frame(gui, borderwidth=0, bg="white")
responseframe.pack()
sframe = Frame(responseframe, padx=3, pady=3, bg="white", highlightbackground="black", highlightthickness=3)
sframe.pack()

statusframe = Frame(sframe, bg="white")
statusframe.pack()

#tabs output
tabControl = ttk.Notebook(responseframe, height=700, width=1200)
tab_1 = Text(tabControl, width=10)
tab_2 = Text(tabControl, width=10)
tab_3 = Text(tabControl, width=10)
tabControl.add(tab_1, text="Raw")
tabControl.add(tab_2, text="Preview")
tabControl.add(tab_3, text="Headers")
tabControl.pack(fill="both")

#status code creation
status = Label(statusframe, text="Status code : 000", height=1, width=16)
status.pack()

#label creation
lbl1 = Text(tab_1, height=1150, width=100, padx=50, pady=50, bg="white", fg="black", font="Helvetica")
lbl1.pack()
lbl2 = HTMLLabel(tab_2, html="preview", height=1150, width=1300, padx=50, pady=50, bg="white", fg="black", font="Helvetica")
lbl2.pack(anchor="center")
lbl3 = Label(tab_3, height=1150, width=1300, padx=50, pady=50, bg="white", fg="black", font="Helvetica")

gui.mainloop()