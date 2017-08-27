#tkinter 2
import tkinter as tk

class App:
    def __init__(self,root):
        frame=tk.Frame(root)
        frame.pack()
        self.hi=tk.Button(root,text='打招呼！',fg='red',command=self.sayhi)
        self.hi.pack(side=tk.LEFT )
    def sayhi(self):
        print("大家好！")

root=tk.Tk()
app=App(root)
root.mainloop()
