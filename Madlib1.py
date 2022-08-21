import tkinter as tk


window = tk.Tk()

def Madlib():
    result.insert(tk.END, e1_value.get())
    result.insert(tk.END, e2_value.get())
    result.insert(tk.END, e3_value.get())
    result.insert(tk.END, e4_value.get())
    result.insert(tk.END, e5_value.get())
    result.insert(tk.END, e6_value.get())
    result.insert(tk.END, e7_value.get())
    result.insert(tk.END, e8_value.get())
    result.insert(tk.END, e9_value.get())
    result.insert(tk.END, e10_value.get())

intstruction=tk.Label(window, text="\nThis is a madlib game about the functions of the parts of the body.\
\nEnter 10 parts of the body and see at the end\
 if you were able \nto match the part to the right function....ENJOY!!!!!!!!\n")
intstruction.grid(row=0,column=1, rowspan=1,)

body_part_1=tk.Label(window, text="Body Part 1")
body_part_1.grid(row=1,column=0)
e1_value=tk.StringVar()
body_part_1_entry=tk.Entry(window, textvariable=e1_value)
body_part_1_entry.grid(row=1,column=1)

body_part_2=tk.Label(window, text="Body Part 2")
body_part_2.grid(row=3,column=0)
e2_value=tk.StringVar()
body_part_2_entry=tk.Entry(window, textvariable=e2_value)
body_part_2_entry.grid(row=3,column=1)

body_part_3=tk.Label(window, text="Body Part 5")
body_part_3.grid(row=5,column=0)
e3_value=tk.StringVar()
body_part_3_entry=tk.Entry(window, textvariable=e3_value)
body_part_3_entry.grid(row=5,column=1)

body_part_4=tk.Label(window, text="Body Part 4")
body_part_4.grid(row=7,column=0)
e4_value=tk.StringVar()
body_part_4_entry=tk.Entry(window, textvariable=e4_value)
body_part_4_entry.grid(row=7,column=1)

body_part_5=tk.Label(window, text="Body Part 5")
body_part_5.grid(row=9,column=0)
e5_value=tk.StringVar()
body_part_5_entry=tk.Entry(window, textvariable=e5_value)
body_part_5_entry.grid(row=9,column=1)

body_part_6=tk.Label(window, text="Body Part 6")
body_part_6.grid(row=11,column=0)
e6_value=tk.StringVar()
body_part_6_entry=tk.Entry(window, textvariable=e6_value)
body_part_6_entry.grid(row=11,column=1)

body_part_7=tk.Label(window, text="Body Part 7")
body_part_7.grid(row=13,column=0)
e7_value=tk.StringVar()
body_part_7_entry=tk.Entry(window, textvariable=e7_value)
body_part_7_entry.grid(row=13,column=1)

body_part_8=tk.Label(window, text="Body Part 8")
body_part_8.grid(row=15,column=0)
e8_value=tk.StringVar()
body_part_8_entry=tk.Entry(window, textvariable=e8_value)
body_part_8_entry.grid(row=15,column=1)

body_part_9=tk.Label(window, text="Body Part 9")
body_part_9.grid(row=17,column=0)
e9_value=tk.StringVar()
body_part_9_entry=tk.Entry(window, textvariable=e9_value)
body_part_9_entry.grid(row=17,column=1)

body_part_10=tk.Label(window, text="Body Part 10")
body_part_10.grid(row=19,column=0)
e10_value=tk.StringVar()
body_part_10_entry=tk.Entry(window, textvariable=e10_value)
body_part_10_entry.grid(row=19,column=1)

button1=tk.Button(window, text="DONE", command=Madlib)
button1.grid(row=20,column=2, )

result=tk.Text(window, width=50)
result.grid(row=21, column=1)

body_part1 = input("Body Part1: \n")
body_part2 = input("Body Part2: \n")
body_part3 = input("Body Part3: \n")
body_part4 = input("Body Part4: \n")
body_part5 = input("Body Part5: \n")
body_part6 = input("Body Part6: \n")
body_part7 = input("Body Part7: \n")
body_part8 = input("Body Part8: \n")
body_part9 = input("Body Part9: \n")
body_part10 = input("Body Part10: \n")  

f"  I think with my {body_part1}. \n\
I run with my {body_part2}. \n\
I eat with my {body_part3}. \n\
I smell with my {body_part4}. \n\
I hear with my {body_part5}. \n\
I taste with my {body_part6}.\n\
I poop with my {body_part7}. \n\
I chew with my {body_part8}. \n\
I clap with my {body_part9}. \n\
I sit with my {body_part10}. \n"



#print(Madlib)



window.mainloop()