from tkinter import *
from tkinter import ttk
import tkinter as tk
from back_end import *
from bs4 import BeautifulSoup as bs
from pywebcopy import save_website
from tkhtmlview import HTMLLabel
from tkinter import messagebox

gui = Tk()
gui.title("TASK")
gui.geometry("1200x520")
gui.config(bg= "lemonchiffon", highlightcolor="red", highlightthickness=10, borderwidth=4)

first_frame = Frame(gui ,borderwidth=0, bg="lemonchiffon")
first_frame.pack(fill = "x")

second_frame=Frame(first_frame, borderwidth=0, pady=30, padx=10, bg= "light green", width=1000, height=120, highlightbackground="black", highlightthickness=2)
second_frame.pack(side = "top")

third_frame=Frame(first_frame, width=800, bg="black", padx=5, pady=5)
third_frame.pack(side = "bottom", pady=15)

response_frame=Frame(gui, borderwidth= 0, bg= "aqua", highlightbackground="black", highlightthickness=4)
response_frame.pack(side = "bottom", pady=20)
sframe = Frame(response_frame, padx=3, pady=3, bg="gold", highlightbackground="gold", highlightthickness=2)
sframe.pack()
status_frame = Frame(sframe, bg="#fff")
status_frame.pack(fill = "both")

def dropdowns():
    newvar = dropdown.get()
    return (newvar)

def saveinput():
    url = input.get(1.0, "end-1c")
    auth = tab_2.get(1.0, "end-1c")
    head = tab_3.get(1.0, "end-1c")
    param = tab_1.get(1.0, "end-1c")
    jsons = tab_4.get(1.0, "end-1c")
    drop = dropdowns()
    code, Text, header = request(drop, url, auth, head, param, jsons)
    soup = bs(Text, "html.parser")
    prettyHTML = soup.prettify()
    tab1.delete("1.0", "end")
    tab1.insert(tk.END, prettyHTML)
    tab2.set_html(Text)
    tab3.delete("1.0", "end")
    tab3.insert(tk.END, header)
    status.config(text="Status_code : " + str(code))
    
def saveproject():
    link = input.get(1.0, "end-1c")
    save_website(url = link, project_folder="./saved_folder/")
    messagebox.showinfo("Success!","Project folder is saved")

btn1 = Button(second_frame, text = "Send", command=saveinput, padx=18, pady=15, bg="#1338be", fg="#fff")
btn1.grid(row=0, column=2)
btn2 = Button(second_frame, text = "Save", command=saveproject, padx=18, pady=15, bg="#1338be", fg="#fff")
btn2.grid(row=0, column=4)

input = Text(second_frame, height=1, pady=20, padx=20, width=80, font=('Times New Roman',15,'normal'), bg = "black", fg = "yellow", insertbackground="yellow")
input.grid(row=0, column=1, padx=45)


options= {
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
}
dropdown = StringVar()
dropdown.set( "GET" )
menu = OptionMenu(second_frame , dropdown, *options)
menu.grid(row = 0, column = 0)
menu.config(bg = "#1338BE", fg="#fff" , padx = 20, pady = 10)

tabcontrol = ttk.Notebook(third_frame, height= 180, width=800)
tab_1 = Text(tabcontrol, width = 100)
tab_2 = Text(tabcontrol, width = 100)
tab_3 = Text(tabcontrol, width = 100)
tab_4 = Text(tabcontrol, width = 100)
tabcontrol.add(tab_1, text='PARAMS')
tabcontrol.add(tab_2, text='AUTHORIZATION')
tabcontrol.add(tab_3, text='HEADERS')
tabcontrol.add(tab_4, text='JSON')
tabcontrol.pack(fill="both")

tabcontrol=ttk.Notebook(response_frame, height=300, width=1200)
tab1=Text(tabcontrol, bg="#EDE9E8", fg= "dark blue")
tab2=HTMLLabel(tabcontrol, html="Preview")
tab3=Text(tabcontrol, bg="#EDE9E8", fg = "red")
tabcontrol.add(tab1, text="RAW")
tabcontrol.add(tab2, text="PREVIEW")
tabcontrol.add(tab3, text="HEADERS")
tabcontrol.pack(fill = "both", padx=40, pady=10)

status = Label(status_frame, text = "Status_code : 000", font= ('Arial', 12, 'bold'), height = 1, width=20)
status.pack()

gui.mainloop()