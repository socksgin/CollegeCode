from tkinter import *
import threading
from time import *
from math import *

class Sat:
    def __init__(self,x,y,vx,vy,dt):
        self.x = x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.dt=dt
        
        
        


    def move(self):
        global ge,s
        self.x = self.x + self.vx*self.dt
        self.y = self.y + self.vy*self.dt
        r3 = (self.x*self.x+self.y*self.y)**(3/2)
        ax = ge/r3*self.x
        ay = ge/r3*self.y
        self.vx = self.vx+ax*self.dt
        self.vy = self.vy+ay*self.dt
        velocity = sqrt(self.vx**2+self.vy**2)
        velocity = "%.2f" % round(velocity,2)
        v.config(text='velocity ' +str(velocity) + " m/s")
        radius = sqrt(s.x**2 + s.y**2)
        r.config(text='radius ' +str(radius) + "m")
        #velocity and radius float 
        
       

class Plot:
    def __init__(self,rw,rh, cw, ch,x,y,sz):
        self.hs = cw/rw
        self.vs = ch/rh
        self.colc = cw/2
        self.rowc = ch/2
        self.sz = sz
        col = self.colc + self.hs*x
        row = self.rowc - self.vs*y
        self.item = can.create_rectangle(col,row,col+sz,row+sz,fill='white')

    def plot(self,x,y):
        global can,s

        col = self.colc + self.hs*x
        row = self.rowc - self.vs*y
        can.coords(self.item,col,row,col+self.sz,row+self.sz)
        #can.move(self.item,-3,-2)

class App:
    def __init__(self,master,s,plt):
        self.master = master
        self.s = s
        self.plt = plt
        self.id = None
        self.poll()

    def poll(self):
        global flag, seconds
        if not flag:
            self.master.after_cancel(self.id)
            return
        self.s.move()
        self.plt.plot(self.s.x,self.s.y)
        self.id= self.master.after(10,self.poll)
        seconds = seconds + s.dt
        ns = "%.0f" % round (seconds,0)
        t.config(text='seconds ' +str(ns) + 's')
        #time

    

def startStop():
    global flag,s,plt
    if flag:
        flag=False
        btn.config(text='Start')
    else:
        flag=True
        btn.config(text='Stop')
        app = App(can,s,plt)
       

flag=False
ge = -6371000**2*9.798
#set up satelite


rt = Tk()



f1 = Frame(rt)
f1.pack(side='top')
f2 = Frame(rt)
f2.pack(side='top')
f3 = Frame(rt)
f3.pack(side='top')


t = Label(f1, text="time",relief=RAISED,width=20,anchor=W)
t.pack(side='left')

r = Label(f1, text='radius',relief=RAISED,width=20,anchor=W)
r.pack(side='left')

v = Label(f2, text='velocity',relief=RAISED,width=20,anchor=W)
v.pack(side='bottom')

seconds = 0

rt.title("Satelite Orbit")

can = Canvas(f3,width=400,height=400,bg='black')
can.pack(side='top')

s = Sat(0,6531000,-7800,0,10)
plt = Plot(14e6,14e6,400,400,0,6531000,2)

can.create_oval(100, 100, 300, 300, outline="darkgreen", 
        fill="green", width=2)


btn = Button(rt,text='start',command=startStop)
btn.pack(side='top')
rt.mainloop()
