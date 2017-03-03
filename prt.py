#print all the numbers in the plugged in list

def prt(lst):
    for i in lst:
        print(i)
    for i in range(len(lst)-1,-1,-1):
        print(lst[1])
    

def rPrt(lst):
    if lst!=[]:
        print(lst[0])
        rPrt(lst[1:])

def rrPrt(lst):
    if lst!=[]:
        rrPrt(lst[1:])
        print(lst[0])
    
    
rrPrt([1,2,3])



