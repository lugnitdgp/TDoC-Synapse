from tkinter import *
from tkinter import ttk


gui = Tk()
gui.title("Synapse")
gui.geometry("900x400")
gui.config(bg="cyan")

top_frame = Frame(gui, bg="gray", height=200, width=400)
top_frame.pack(pady=25)

#outputframe = Frame(gui, bg="pink")
#outputframe.pack(anchor="center")
#output = Label(outputframe, text="My output is here", height=2, bg="pink")
#output.pack(padx=200, pady=40)

my_input = Text(top_frame, height=1.5, width=80)
#my_input.pack(anchor="center", padx=45, pady=50)
my_input.grid(row=0, column=1, padx=35, pady=50)

#def Click():
#    status = Label(statusframe, text="Hello", height=1, width=16)
#    status.pack()
def dropdown(self):
    newvar = clicked.get()
    print(newvar)

def saveinput():
    var = my_input.get(1.0, "end-1c")
    tab_1.config(text=var)
    print(var)

btn = Button(top_frame, text="Send", command=saveinput)
btn.grid(row=0, column=2, padx=20)
btn = Button(top_frame, text="Save")
btn.grid(row=0, column=3, padx=20)

options = {
    "GET",
    "PUT",
    "POST",
    "PATCH",
    "DELETE"
}
clicked = StringVar()
clicked.set("GET")
drop = OptionMenu(top_frame, clicked, *options, command=dropdown)
drop.grid(row=0, column=0)
drop.config(bg="darkblue", fg="#fff", padx=20, pady=10)

tabControl = ttk.Notebook(top_frame, height=100, width=400)
tab1 = Text(tabControl, width=100)
tab2 = Text(tabControl, width=100)
tab3 = Text(tabControl, width=100)
tab4 = Text(tabControl, width=100)
tabControl.add(tab1, text="Params")
tabControl.add(tab2, text="Authorization")
tabControl.add(tab3, text="Headers")
tabControl.add(tab4, text="JSON")
tabControl.grid(row=1, column=1, padx=40, pady=45)
#tabControl.pack(fill="both", padx=40, pady=45)

responseframe = Frame(gui, borderwidth=0, bg="#fff")
responseframe.pack()
sframe = Frame(responseframe, padx=3, pady=3, bg="#fff", highlightbackground="black", highlightthickness=3)
sframe.pack()
statusframe = Frame(sframe, bg="#fff")
statusframe.pack()

tabControl = ttk.Notebook(responseframe, height=700, width=1200)
tab_1 = Label(tabControl, text="demo text", bg="#fff")
tab_2 = Label(tabControl, text="preview", bg="#fff")
tab_3 = Label(tabControl, text="", bg="#fff")
tabControl.add(tab_1, text="Raw")
tabControl.add(tab_2, text="Preview")
tabControl.add(tab_3, text="Headers")
tabControl.pack(fill="both")

gui.mainloop()
