from time import *
from _thread import *

def worker(str,delay):
    for i in range(100):
        print(str,end='')
        sleep(delay)
        
start_new_thread(worker, ('ping', .1))
start_new_thread(worker, ('pong', .1))            
