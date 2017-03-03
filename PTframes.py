from tkinter import *

rt = Tk()


f2 = Frame(rt)
f2.pack(side='top')
f1 = Frame(f2)
f1.pack(side='right')


lbla = Label(f1, text='A')
lbla.pack(side='top')

lblb = Label(f2, text='B')
lblb.pack(side='left')

lblc = Label(f1, text='C')
lblc.pack(side='top')

lbld = Label(rt, text='D')
lbld.pack(side='top')

rt.mainloop()
