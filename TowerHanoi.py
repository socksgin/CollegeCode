#towers of Hanoi
n = 4

poles = [[],[],[]]
for i in range(n,0,-1):
    poles[0].append(i)
cnt=0
#number of items to be moved, source pole, destination pole, extra pole
def moveTower(n,s,d,e):
    global cnt
    if n<=1:
        if poles[d]==[] or poles[d][-1]>poles[s][-1]:
            disk = poles[s].pop()
            poles[d].append(disk)
            #print('move disk',disk,'from pole',s,'to pole',d)
            cnt+=1
        else:
            print('ERROR')
    else:
        moveTower(n-1,s,e,d)
        moveTower(1,s,d,e)
        moveTower(n-1,e,d,s)
print(poles)
moveTower(n,0,1,2)
print(poles)
print(cnt)
    
