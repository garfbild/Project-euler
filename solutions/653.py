import time
#currenty working solution but is too slow for final problem

def random(j):
    rList = [6563116]
    r = 6563116
    for i in range(j-1):
        r = (r**2) %32745673
        rList.append(r)
    return rList

def swap(direction):
    if direction == "e":
        return "w"
    else:
        return "e"
    return "fuck"

d = 20 #millimeters
#collisions are elastic
#constant velocity


L = float(100000) #length of tube millimeters of course
N = 101 #number of balls
j = 51 #ball we wnat to track

trackedDistance = 0

randomList = random(N)
#the gaps between the marbles by closest points are given by random function
#first ball center is at random 1 + 10
ballsPosition = []   #list of location of centers of balls from west side of tube
ballsPosition.append((randomList[0]%1000 + 1)+10)
for b in range(1,N):
    ballsPosition.append(ballsPosition[-1] + (randomList[b]%1000 + 1) + d) #next ball position from west side between j and j-1 is r(j) + d

ballsDirection = []
for d in range(N):
    if randomList[d] <= 10000000:
        ballsDirection.append("e") # 1 is east
    else:
        ballsDirection.append("w") # 0 is west

while ballsPosition[j-1] < L:
    if ballsPosition[-1] >= L: # if a ball has fallen out of the tube we delete it
        ballsPosition = ballsPosition[:-1]
        ballsDirection = ballsDirection[:-1]
    potentialDistancesList = []
    for n in range(len(ballsDirection)):
        if ballsDirection[n] == "e":
            if n == len(ballsDirection)-1 or ballsPosition[n+1] == L:
                potentialDistance = L - ballsPosition[n]
            elif ballsDirection[n+1] == "w":
                potentialDistance = abs(ballsPosition[n]-ballsPosition[n+1])/2 - 10
            else:
                potentialDistance = L*2

        if ballsDirection[n] == "w":
            if n == 0:
                potentialDistance = ballsPosition[0] - 10
            elif ballsDirection[n-1] == "e":
                potentialDistance = abs(ballsPosition[n]-ballsPosition[n-1])/2 - 10
            else:
                potentialDistance = L*2

        potentialDistancesList.append(potentialDistance)

    minimumPotentialDistance = min(potentialDistancesList)
    trackedDistance += minimumPotentialDistance

    for m in range(len(ballsDirection)):
        if ballsDirection[m] == "e":
            ballsPosition[m] += minimumPotentialDistance
        else:
            ballsPosition[m] += -minimumPotentialDistance

        if potentialDistancesList[m] == minimumPotentialDistance and ballsPosition[n] != L:
            ballsDirection[m] = swap(ballsDirection[m])


print(trackedDistance)
