import math
import numpy as np

def norm(x):
    return (x[0]**2 + x[1]**2)**0.5

file = open("solutions/triangles.txt","r")
List = file.read().split('\n')
List = [i.split(',') for i in List]
del List[-1]
count = 0
for i in range(len(List)):
    t = List[i]
    print(t)
    a = [int(t[0]),int(t[1])]
    b = [int(t[2]),int(t[3])]
    c = [int(t[4]),int(t[5])]


    s = 0
    adotb = a[0]*b[0] + a[1]*b[1]
    cosTheta = adotb/(norm(a)*norm(b))
    Theta = math.acos(cosTheta)
    s += Theta
    adotc = a[0]*c[0] + a[1]*c[1]
    cosTheta = adotc/(norm(a)*norm(c))
    Theta = math.acos(cosTheta)
    s += Theta
    bdotc = b[0]*c[0] + b[1]*c[1]
    cosTheta = bdotc/(norm(b)*norm(c))
    Theta = math.acos(cosTheta)
    s += Theta

    if s/2 == math.pi:
        count += 1
print(count)
