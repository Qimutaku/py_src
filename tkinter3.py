#tkinter 3
import tkinter as tk

root=tk.Tk()
##alabel=tk.Label(root,text='欢迎来到这里！\n我是长泽雅美')
#alabel.pack(side=tk.LEFT,padx=10)

img=tk.PhotoImage(file='mas.gif')
ilb=tk.Label(root,text='欢迎来到这里！\n我是长泽雅美',image=img,compound=tk.CENTER,fg='white',font=('宋体',20))
#ilb.pack(side=tk.RIGHT)
ilb.pack()
             
tk.mainloop ()
