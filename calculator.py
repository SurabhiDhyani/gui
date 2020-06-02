from tkinter import *
tk=Tk()
tk.title("Calculator")
en=Entry(tk,width=40, borderwidth=5)
en.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

f_num=0
op=""

def button_click(number):
    en.insert(END,number)

def button_clear():
    en.delete(0,END)

def button_add():
    input_num=en.get()
    global f_num
    f_num=float(input_num)
    en.delete(0,END)
    global op
    op="add"
def button_sub():
    input_num = en.get()
    global f_num
    f_num = float(input_num)
    en.delete(0, END)
    global op
    op="sub"

def button_mul():
    input_num=en.get()
    global f_num
    f_num=float(input_num)
    en.delete(0,END)
    global op
    op="mul"

def button_div():
    input_num=en.get()
    global f_num
    f_num=float(input_num)
    en.delete(0,END)
    global op
    op="div"

def button_equal():
    input_num=en.get()
    s_num=float(input_num)
    en.delete(0,END)
    if op=="add":
        en.insert(0,f_num + s_num)
    elif op=="sub":
        en.insert(0,f_num- s_num)
    elif op=="mul":
        en.insert(0,f_num*s_num)
    elif op=="div":
        en.insert(0,f_num/s_num)



    return

button_1=Button(tk,text="1",padx=30, pady=20,command=lambda :button_click(1))
button_2=Button(tk,text="2",padx=30, pady=20,command=lambda :button_click(2))
button_3=Button(tk,text="3",padx=30, pady=20,command=lambda :button_click(3))
button_4=Button(tk,text="4",padx=30, pady=20,command=lambda :button_click(4))
button_5=Button(tk,text="5",padx=30, pady=20,command=lambda :button_click(5))
button_6=Button(tk,text="6",padx=30, pady=20,command=lambda :button_click(6))
button_7=Button(tk,text="7",padx=30, pady=20,command=lambda :button_click(7))
button_8=Button(tk,text="8",padx=30, pady=20,command=lambda :button_click(8))
button_9=Button(tk,text="9",padx=30, pady=20,command=lambda :button_click(9))
button_0=Button(tk,text="0",padx=30, pady=20,command=lambda :button_click(0))
button_add=Button(tk,text="+",padx=30,pady=50,command=button_add)
button_equal=Button(tk,text="=",padx=75,pady=20,command=button_equal)
button_clear=Button(tk,text="C",padx=30,pady=20,command=button_clear)
button_sub=Button(tk,text="-",padx=30,pady=20,command=button_sub)
button_mul=Button(tk,text="X",padx=30,pady=20,command=button_mul)
button_div=Button(tk,text="/",padx=30,pady=20,command=button_div)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=1)
button_add.grid(row=4,column=0,rowspan=2)
button_equal.grid(row=6,column=1,columnspan=2)
button_clear.grid(row=6,column=0)
button_sub.grid(row=4,column=2)
button_mul.grid(row=5,column=2)
button_div.grid(row=5,column=1)


tk.mainloop()