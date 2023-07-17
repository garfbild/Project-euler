import math
import numpy as np
#if we think of each edge as an inequality where the remaining point tells us which
#way the inequality "points" we check all three
def checkLine(Q,W,E):
    a,b = Q[0],Q[1]
    c,d = W[0],W[1]
    x,y = E[0],E[1]
    #xF*x +yF*y = C equation of a line
    xF = b-d
    yF = c-a
    C = b*c-a*d
    if xF*x + yF*y > C:
        if 0 > C:
            return True
        else:
            return False
    else:
        if 0 < C:
            return True
        else:
            return False

file = open("solutions/triangles.txt","r")
List = file.read().split('\n')
List = [i.split(',') for i in List]
del List[-1]
count = 0
for i in range(len(List)):
    t = List[i]
    print(t)
    A = [int(t[0]),int(t[1])]
    B = [int(t[2]),int(t[3])]
    C = [int(t[4]),int(t[5])]
    if checkLine(A,B,C):
        if checkLine(C,A,B):
            if checkLine(B,C,A):
                print("yes")
                count += 1

print(count)
