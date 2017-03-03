import random
#on average, at the end of the walk where is the person?
#rep is number of random walks
#numStep is number of steps in each random walk

def main(reps, numStep):
    for i in range(reps):
        total = 0
        pos = walk(numStep)
        total += pos
    print(total/reps)

#returns final position
def walk(numStep):
    pos = 0
    for i in range(numStep):
        pos += step()
    return pos

#returns randomly a 1 or a -1
def step():
    r = random.random()
    if r<.5:
        return -1
    else:
        return 1
