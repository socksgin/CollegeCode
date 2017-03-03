from tkinter import *

rt= Tk()

f3 = Frame(rt)
f3.pack(side='top')
f1 = Frame(f3)
f1.pack(side='left')
f2 = Frame(f3)
f2.pack(side='top')


lblE = Label(f1,text='E',bg='pink')
lblE.pack(side='top')

lblF = Label(f1,text='F',bg='cyan')
lblF.pack(side='top')

lblG = Label(f2,text='G',bg='lightgreen')
lblG.pack(side='left')

lblH = Label(f2,text='H',bg='blue')
lblH.pack(side='top')

lblI = Label(f2,text='I',bg='orange')
lblI.pack(side='top')

lblJ = Label(f2, text='J',bg='purple')
lblJ.pack(side='top')

lblK = Label(rt, text='K',bg='red')
lblK.pack(side='top')

rt.mainloop()
