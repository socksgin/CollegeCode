def perm(lst, c = [], x = 0):
    i = -1
    g = len(lst) - 1
    if x == g:
        while i < g:
            i += 1
            if lst[i] in c:
                continue
            c.append(lst[i])
            print(c)
            del c[-1]
            i = g
    else:
        while i < g:
            if x == 0:
                del c[:]
            elif g == x:
                del c[-1]
            elif len(c) > x:
                del c[-1]
                continue
            i += 1
            if lst[i] in c:
                continue
            c.append(lst[i])
            x + 1
            perm(lst, c, x + 1)

perm([1,2,3,4])
