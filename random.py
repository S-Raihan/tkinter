import tkinter as tk
import random

def roll():
	lbl_value["text"] = str(random.randint(0,100))

window = tk.Tk()

window.rowconfigure([0,1],minsize = 100,weight =1)
window.columnconfigure(0,minsize =100,weight=1)

lbl1 = tk.Button(master=window,text="Roll",command=roll)
lbl1.grid(row=0,column = 0,sticky="nsew")

lbl_value = tk.Label(master = window,text="0")
lbl_value.grid(row=1,column=0,sticky="nsew")

window.mainloop()