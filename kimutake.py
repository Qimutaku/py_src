#kimutaku
import tkinter as tk

root=tk.Tk()
root.title('KIMURA TAKUYA')

alabel=tk.Label(root,text='欢迎\n我是木村')
alabel.pack(side=tk.LEFT)

img=tk.PhotoImage(file='kimutaku.gif')
imglabel=tk.Label(root,image=img)
imglabel.pack(side=tk.RIGHT )

root.mainloop()
