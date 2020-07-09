import random
import time

def CommunityChest():
    r = random.randint(1,16)
    if r == 1:
        return "GO"
    elif r == 2:
        return "JAIL"
    else:
        return "NONE"

def Chance():
    r = random.randint(1,16)
    if r == 1:
        return "GO"
    elif r == 2:
        return "JAIL"
    elif r == 3:
        return "C1"
    elif r == 4:
        return "E3"
    elif r == 5:
        return "H2"
    elif r == 6:
        return "R1"
    elif r == 7 or r == 8:
        return "R*"
    elif r == 9:
        return "U*"
    elif r == 10:
        return "GB3"
    else:
        return "NONE"


board = ["GO","A1","CC1","A2","T1","R1","B1","CH1","B2","B3","JAIL","C1","U1","C2","C3","R2","D1","CC2","D2","D3","FP","E1","CH2","E2","E3","R3","F1","F2","U2","F3","G2J","G1","G2","CC3","G3","R4","CH3","H1","T2","H2"]
boardCount = []
dict = {}
for i in range(len(board)):
    dict[board[i]] = i
    boardCount.append(0)

DiceSides = 4
position = 0
DoubleCount = 0
Tstart = time.time()
while time.time() - Tstart <= 4:
    roll1 = random.randint(1,DiceSides)
    roll2 = random.randint(1,DiceSides)
    position += roll1+roll2

    if position >= len(board):
        position += -len(board)

    if board[position][0:2] == "CC":
        Action = CommunityChest()
        if Action != "NONE":
            position = dict[str(Action)]

    if board[position][0:2] == "CH":
        Action = Chance()
        if Action != "NONE":
            if Action == "GB3":
                position += -3
            elif Action == "U*":
                if position > 12 and position <= 28:
                    position = 28
                else:
                    position = 12
            elif Action == "R*":
                if position < 5:
                    position = 5
                elif position < 15:
                    position < 15
                elif position < 25:
                    position = 25
                elif position < 35:
                    position = 35
                else:
                    position = 5
            else:
                position = dict[Action]

    if board[position] == "G2J":
        position = 10

    if roll1 == roll2:
        DoubleCount += 1
    else:
        DoubleCount = 0

    if DoubleCount == 3:
        position = 10

    boardCount[position] += 1

print(boardCount)
maxlist = []
for i in range(3):
    max = 0
    maxj = 0
    for j in range(len(boardCount)):
        if boardCount[j] > max and j not in maxlist:
            max = boardCount[j]
            maxj = j
    maxlist.append(maxj)

print(maxlist)
