#button

from tkinter import *
def call():
    var1.set('wtf')

root=Tk()
frame1=Frame(root)
frame2=Frame(root)
var1=StringVar()
var1.set('your name')
textLabel=Label(frame1,textvariable=var1,justify=LEFT)
textLabel.pack(side=LEFT)

pht=PhotoImage(file='mas.gif')
iml=Label(frame1,image=pht)
iml.pack(side=RIGHT)

tButton=Button(frame2,text='yes',command=call)
tButton.pack()
frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()
