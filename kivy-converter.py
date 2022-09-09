import tkinter as tk

#from sqlalchemy import column 

window = tk.Tk()

def conversions():
    gram=float(e1_value.get())*1000
    t1.delete("1.0",tk.END)
    t1.insert(tk.END,gram)

    pounds=float(e1_value.get())*2.20462
    t2.delete("1.0",tk.END)
    t2.insert(tk.END,pounds)

    ounces=float(e1_value.get())*35.274 
    t3.delete("1.0",tk.END)
    t3.insert(tk.END,ounces)


unit=tk.Label(window, text="ENTER NUMBER IN KG")
unit.grid(row=0,column=0)
b1 = tk.Button(window, text="convert", command=conversions)
b1.grid(row=0,column=3)

e1_value=tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

l_1=tk.Label(window, text="GRAM")
l_1.grid(row=1,column=0)

t1 = tk.Text(window,height=2,width=20)
t1.grid(row=2,column=0)

l_2=tk.Label(window, text="POUND")
l_2.grid(row=1,column=1)

t2 = tk.Text(window,height=2,width=20)
t2.grid(row=2,column=1)

l_3=tk.Label(window, text="OUNCE")
l_3.grid(row=1,column=3)

t3 = tk.Text(window,height=2,width=20)
t3.grid(row=2,column=3)

window.mainloop()