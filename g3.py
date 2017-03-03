from tkinter import *

def chnColor():
    de.configure(bg=de.get())
    
def mkBox(e):
    x0 = e.x-5
    y0 = e.y-5
    x1 = e.x+5
    y1 = e.y+5
    can.create_rectangle(x0,y0,x1,y1,fill='yellow')
        

rt = Tk()
lbl = Label(rt, text ="Color")
lbl.pack(side="top")
rt.title("Color Chooser")

btn = Button(rt, text="Change Color", command=chnColor)
btn.pack(side='top')
can = Canvas(rt,width=300,height=300,bg='green')
can.pack(side='top')
can.bind("<Button-1>",mkBox)
         
rt.mainloop()
