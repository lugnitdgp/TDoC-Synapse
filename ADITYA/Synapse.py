import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as Tk
from backend import *
from bs4 import BeautifulSoup as bs
from tkinter import messagebox


frame = Tk()
# gui logic
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
    url = inputtxt.get(1.0, "end-1c")
    auth = tab2.get(1.0, "end-1c")
    head = tab3.get(1.0, "end-1c")
    drop = dropdown()
    code, text, header = request(drop, url, auth, head)
    soup = bs(text, 'html.parser')
    prettyHTML = soup.prettify()
    lbl1.delete("1.0", "end")
    lbl1.insert(Tk.END, prettyHTML)
    lbl2.set_html(text)
    status.config(text="Status Code :" + str(code))
    
def saveproject():
    link = inputtxt.get(1.0, "end-1c")
    savewebsite(url=link, project_folder="./saved_folder/")
    messagebox.showinfo("Success!!", "Project folder saved")

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

# Button creation
sendButton = Button(fr2, text="Send", padx=18, pady=15, bg="blue", fg="black", command=saveinput)
sendButton.grid(row=0, column=2)
saveButton = Button(fr2, text="Save", padx=18, pady=15, bg="blue", fg="black")
saveButton.grid(row=0, column=4)
tabControl = ttk.Notebook(statusframe)
statusframe.grid(row=4, column=4)




tabControl= ttk.Notebook(responseframe, height = 700, width = 1200)
tab_1 = Label(tabControl, text="", bg="#fff")
tab_2 = Label(tabControl, text="", bg="#fff")
tab_3 = Label(tabControl, text="", bg="#fff")


tabControl.add(tab_1, text='Raw')
tabControl.add(tab_2, text='Preview')
tabControl.add(tab_3, text='Headers')

tabControl.pack(fill = "both")

status = Label(statusframe, text= "Status Code: 000", height=1, width=16)
status.pack()

# Label Creation
lbl1 = Label(tab_1, text="raw", height=1150, width=100, padx=50, pady=50, bg="#fff", fg="black", font="Helvetica")
lbl1.pack()
lbl2 = Label(tab_2, html="Preview", height=1150, width=1300, padx=50, pady=50, bg="#fff", fg="black", font="Helvetica")
lbl1.pack(anchor = "center")
lbl1 = Label(tab_1, text="raw", height=1150, width=1300, padx=50, pady=50, bg="#fff", fg="black", font="Helvetica")
lbl1.pack()



frame.mainloop()
