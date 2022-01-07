import tkinter as tk

window = tk.Tk()




window.title("Address Provider")


frm_set = tk.Frame(relief = tk.RAISED, borderwidth = 3)
frm_set.pack(padx = 10, pady = 10)


#create address

lebels_set  = [
    "First Name: ",
    "Last Name: ",
    "ID No: ",
    "Semester: ",
    "Section: ",
    "Email: ",
    "Contact No: ",
    "City: ",
    "Country: "
]

for id , lset in enumerate(lebels_set):
    lebel = tk.Label(master=frm_set,text = lset)
    ent = tk.Entry(master=frm_set,width = 70)
    lebel.grid(row = id, column = 0, sticky="e",padx = 5,pady = 5)
    ent.grid(row = id, column = 1,padx = 5,pady = 5)



button = tk.Frame()
button.pack(fill = tk.X,padx = 5, pady = 5)

submit = tk.Button(master=button,text ="Submit")
submit.pack(side = tk.RIGHT,padx = 10, ipadx =30)
reset = tk.Button(master=button,text ="Reset")
reset.pack(side = tk.RIGHT,padx = 10, ipadx =30)



























window.mainloop()