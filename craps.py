from tkinter import *
from math import *
import random
'''
Joseph Dylan Sachtjen
CS 201 2PM Class
'''

def throw():
    a = random.randint(1,6)
    b = random.randint(1,6)
    return a+b

def main(numGames):
    totalWins=0
    for i in range(numGames):
        numWins = playOneGame()
        if numWins != False:
            totalWins = totalWins + numWins

    print(totalWins/numGames)
    print(totalWins)

def playOneGame():
    point = 0
    wins = 0
    t = throw()
    if t==2 or t==3 or t==12:
        return False
    elif t==7 or t==11:
        wins = 1
        return wins
    else:
        wins = throws(point)
        return wins

    
def throws(point):
    wins = 0
    status = True
    while status != False:
        newRoll = throw()
        if newRoll == point:
            wins+=1
            return wins
        if newRoll == 7:
            status = False
            return False
        

numWins = 0
main(10000)

