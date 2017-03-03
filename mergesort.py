def mergeSort(lst):
    n = len(lst)
    if n<=1:
        return
    m = n//2
    lst1 = lst[:m]
    lst2 = lst[m:]
    mergeSort(lst1)
    mergesort(lst2)
    merge(lst1,lst2,lst)

def merge(lst1,lst2,lst):
    n1 = len(lst1)
    n2 = len(lst2)
    i1 = i2 = i = 0
    while i1<n1 and i2<n2:
        if lst1[i1]<lst2[i2]:
            lst[i] = lst[i1]
            i1 +=1
        else:
            lst[i] = lst2[i2]
            i2 +=1
        i +=1
        while i1<n1:
            lst[i]=lst1[i1]
            i += 1
            i1  += 1
            
        while i2<n2:
            lst[i]=lst1[i2]
            i += 1
            i2  += 1
