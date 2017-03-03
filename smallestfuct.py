def smallest(array):
    if len(array)==0:
        return

    if len(array)==1:
        return array[0]

    v = array[0]
    x = smallest(array[1:])
    if v < x:
        return v


    return x


v = 0
x = 0
a = [2,5,17,8]
print(smallest(a))
