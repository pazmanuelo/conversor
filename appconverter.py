'''Tkinter'''
from tkinter import *
from tkinter import ttk

def calculo(*args):
    try:
        num1 = float(temp.get())
        farenheit.set(num1*1.8+32)
    except ValueError:
        pass

root = Tk()
root.title("Celsios a Farenheit")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

temp = StringVar()
farenheit = StringVar()

tempEntry = ttk.Entry(mainframe, width=7, textvariable=temp)
tempEntry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=farenheit).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calcular", command=calculo).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="ªC").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="ªF").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()#a
