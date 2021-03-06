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

def calculatePotentialDistance(ballsPosition,ballsDirection,n):
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
    return ballsPosition,ballsDirection,potentialDistance

d = 20 #millimeters
#collisions are elastic
#constant velocity


L = float(100000) #length of tube millimeters of course
N = 101 #number of balls
j = 51 #ball we want to track

# L = float(1000000000)
# N = 1000001
# j = 500001
#minimumPotentialDistance is always 0.5

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

potentialDistancesList = []
for e in range(N):
    ballsPosition,ballsDirection,potentialDistance = calculatePotentialDistance(ballsPosition,ballsDirection,e)
    potentialDistancesList.append(potentialDistance)

while ballsPosition[j-1] < L:
    if ballsPosition[-1] >= L: # if a ball has fallen out of the tube we delete it
        ballsPosition = ballsPosition[:-1]
        ballsDirection = ballsDirection[:-1]
        potentialDistancesList = potentialDistancesList[:-1]
        N += -1
    elif ballsDirection[-1] == "e" and N != j: # if the easternly most ball is heading east we delete it
        ballsPosition = ballsPosition[:-1]
        ballsDirection = ballsDirection[:-1]
        potentialDistancesList = potentialDistancesList[:-1]
        N += -1
    elif ballsDirection[-1] == "e" and N == j: # if the eastern most ball is the ball we are tracking we know it will end by covering the remaining distance and so we break
        trackedDistance += L - ballsPosition[-1]
        break

    minimumPotentialDistance = min(potentialDistancesList) # the most amount of distance all balls can travel without missing any collisions
    trackedDistance += minimumPotentialDistance
    for m in range(N):
        if ballsDirection[m] == "e":
            ballsPosition[m] += minimumPotentialDistance
        else:
            ballsPosition[m] += -minimumPotentialDistance

        if potentialDistancesList[m] == minimumPotentialDistance: # bouncing routine
            ballsDirection[m] = swap(ballsDirection[m])

        potentialDistancesList[m] += -minimumPotentialDistance

    for k in range(N): # if the ball just bounced and has no potentialDistance we must recaluate it for the ball and its neighbour potentially
        if potentialDistancesList[k] == float(0):
            ballsPosition,ballsDirection,potentialDistance = calculatePotentialDistance(ballsPosition,ballsDirection,k)
            potentialDistancesList[k] = potentialDistance
            if k != N-1 and ballsDirection[k] == "e" and ballsDirection[k+1] == "w":
                ballsPosition,ballsDirection,potentialDistance = calculatePotentialDistance(ballsPosition,ballsDirection,k+1)
                potentialDistancesList[k+1] = potentialDistance
            elif k != 0 and ballsDirection[k] == "w" and ballsDirection[k-1] == "e":
                ballsPosition,ballsDirection,potentialDistance = calculatePotentialDistance(ballsPosition,ballsDirection,k-1)
                potentialDistancesList[k-1] = potentialDistance



print(trackedDistance)
