from tkinter import *
from tkinter import ttk

gui = Tk()
gui.title("TASK")
gui.geometry("1200x520")
gui.config(bg= "#CCCCFF", highlightbackground="NAVY BLUE", highlightcolor="NAVY BLUE", highlightthickness=10 )

first_frame = Frame(gui ,borderwidth=0, bg="#CCCCFF")
first_frame.pack(fill = "x")

second_frame=Frame(first_frame, borderwidth=0, pady=30, bg= "#F0FFFF",width=1000)
second_frame.pack(anchor = "center")

response_frame=Frame(gui, borderwidth= 0, bg= "#CCCCFF")
response_frame.pack()
sframe = Frame(response_frame, padx=3, pady=3, bg="lemonchiffon", highlightbackground="black", highlightthickness=2)
sframe.pack()
status_frame = Frame(sframe, bg="#fff")
status_frame.pack(fill = "both")

def dropdowns(self):
    var1 = dropdown.get()
    print(var1)

def saveinput():
    var2 = input.get(1.0, "end-1c")
    print(var2)
    var3 = tab_1.get(1.0, "end-1c")
    print(var3)
    var4 = tab_2.get(1.0, "end-1c")
    print(var4)
    var5 = tab_3.get(1.0, "end-1c")
    print(var5)
    var6 = tab_4.get(1.0, "end-1c")
    print(var6)
    tab1.config(text=var2)

btn1 = Button(second_frame, text = "Send", command=saveinput, padx=18, pady=15, bg="#1338be", fg="#fff")
btn1.grid(row=0, column=2)
btn2 = Button(second_frame, text = "Save", padx=18, pady=15, bg="#1338be", fg="#fff")
btn2.grid(row=0, column=4)

input = Text(second_frame, height=2, width=70)
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
drop = OptionMenu(second_frame , dropdown, command=dropdowns, *options)
drop.grid(row = 0, column = 0)
drop.config(bg = "#1338BE", fg="#fff" , padx = 20, pady = 10)

tabcontrol = ttk.Notebook(first_frame, height= 120, width=800)
tab_1 = Text(tabcontrol, width = 100)
tab_2 = Text(tabcontrol, width = 100)
tab_3 = Text(tabcontrol, width = 100)
tab_4 = Text(tabcontrol, width = 100)
tabcontrol.add(tab_1, text='PARAMS')
tabcontrol.add(tab_2, text='AUTHORIZATION')
tabcontrol.add(tab_3, text='HEADERS')
tabcontrol.add(tab_4, text='JSON')
tabcontrol.pack(fill="both", padx=40, pady=30)

tabcontrol=ttk.Notebook(response_frame, height=300, width=1000)
tab1=Label(tabcontrol, text="", bg="#fff")
tab2=Label(tabcontrol, text="", bg="#fff")
tab3=Label(tabcontrol, text="", bg="#fff")
tabcontrol.add(tab1, text="RAW")
tabcontrol.add(tab2, text="PREVIEW")
tabcontrol.add(tab3, text="HEADERS")
tabcontrol.pack(fill = "both", padx=40, pady=10)

status = Label(status_frame, text = "status_code :000", height = 1, width=20)
status.pack()
gui.mainloop()