def dotProduct(a,b):
    return a[0]*b[0] + a[1]*b[1]

laserstart = [0.0,10.1]
impact = [1.4,-9.6]
laserdir = [impact[1]-laserstart[1],impact[0]-laserstart[0]]
wallgradient = -4*impact[0]/impact[1]
inverse = -1/wallgradient
#compute normal
dy = (1/(inverse**2 + 1))**0.5
dx = 1-dy**2
normal = [dx,dy]
reflection = laserdir - 2*dotProduct(laserdir,normal)*normal
print(reflection)
