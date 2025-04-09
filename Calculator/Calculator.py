from tkinter import *
def add():
    ans.delete(0,END)
    a=int(box1.get())
    b=int(box2.get())
    c=a+b
    ans.insert(0,c)
def sub():
    ans.delete(0,END)
    a=int(box1.get())
    b=int(box2.get())
    c=a-b
    ans.insert(0,c)
def mul():
    ans.delete(0,END)
    a=int(box1.get())
    b=int(box2.get())
    c=a*b
    ans.insert(0,c)
def div():
    ans.delete(0,END)
    a=int(box1.get())
    b=int(box2.get())
    c=a/b
    ans.insert(0,c)
def clear():
    ans.delete(0,END)
    box1.delete(0,END)
    box2.delete(0,END)
page = Tk() 
page.title("Calculator")
page.geometry('300x300')
a = Label(page, text = "'Simple Calculator'", font='Times 18').grid(row=0, columnspan=2)
Label(page,text="INPUT-1:",width=8, font='Times 12').grid(row=1)
Label(page, text="INPUT-2:",width=8,font='Times 12').grid(row=2)
Label(page, text="ANSWER:", width=8, font='Times 12').grid(row=3, column=1)
box1=Entry(page,font='Times 14')
box2=Entry(page,font='Times 14')
ans=Entry(page,width=10 ,font='Times 25')
box1.grid(row= 1, column=1)
box2.grid(row=2, column=1)
ans.grid(row=4, column=1)
add = Button(page, text="Add(+)", width=5,font='Times 12', command=add).grid(row=4,column=0)
sub = Button(page, text="Sub(-)", width=5,font='Times 12', command=sub).grid(row=5,column=0)
mul = Button(page, text="Mul(*)", width=5,font='Times 12', command=mul).grid(row=6,column=0)
div = Button(page, text="Div(/)", width=5,font='Times 12', command=div).grid(row=7,column=0)
clear = Button(page, text="Clear", padx=10,pady=5,font='Times 12',command=clear).grid(row=7,column=1)
page.mainloop()
