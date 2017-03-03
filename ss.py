#return the index of the smallest value from [start:]
def posMin(lst,start):
    n = len(lst)
    firstval =lst[start]
    pos = start
    for i in range(start,n):
        if lst[i]<firstval:
            first = lst[i]
            pos = i
    return pos

def selectionSort(lst):
    n = len(lst)
    for start in range(n-1):
        p = posMin(lst,start)
        lst[start],lst[p] = lst[p],lst[start]


    
        
