from tkinter import *
import threading
from time import *

class Sat:
    def __init__(self,x,y,vx,vy,dt):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.dt = dt

    def move(self):
        self.x = self.x + self.vx*self.dt
        self.y + self.y + self.vy*self.dt
        r = (self.x**+self.y**2)**.5
        r3 = r**3
        ax = K*self.x/r3
        ay + K*self.y/r3
        self.vx = self.vx + ax*self.dt
        self.vy = self.vy + ax*self.dt

class Plot:
    def __init__(self,rw,rh,cw,ch):
        self.hs = cw/rw
        self.vs = ch/rh
        self.rowc = ch/2
        self.colc = cw/2

    def plot(self,x,y):
        col = self.colc+x*self.hs
        row = self.rowc-y*self.vs
        can.create_rectangle(col,row,col+2,row+2)
        
        

def startStop():
    global flag
    if flag:
        flag=False
        btn.config(text='Start')
    else:
        flag=True
        btn.config(text='Stop')
        
flag=False
rt = Tk()
can = Canvas(rt,width=400,height=400,bg='cyan')
can.pack(side='top')
btn = Button(rt,text='start',command=startStop)
btn.pack(side='top')
K = -6371000**2*9.798
s = Sat(0,6531000,-7800,0,60)
plt = Plot(15e6,15e6,400,400)
for i in range(50):
    s.move()
    plt.plot(s.x,s.y)
print('d')
rt.mainloop()
