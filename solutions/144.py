laserstart = [0.0,10.1]
impact = [1.4,-9.6]
laserdirection = [impact[1]-laserstart[1],impact[0]-laserstart[0]]
wallgradient = -4*impact[0]/impact[1]
normal = 1/wallgradient
#compute normal
print(wallgradient,normal)
b = (1/(normal**2 + 1))**0.5
a = 1-b**2
print(a,b)
