def dotProduct(a,b):
    return a[0]*b[0] + a[1]*b[1]

laserstart = [0.0,10.1]
impact = [1.4,-9.6]
laserdir = [impact[0]-laserstart[0],impact[1]-laserstart[1]]
print(laserdir)
wallgradient = -4*impact[0]/impact[1]
print(wallgradient)
inverse = -1/wallgradient

#compute normal
normal = [1,inverse]
print(normal)
reflection = [laserdir[0] - 2*dotProduct(laserdir,normal)*normal[0],laserdir[1] - 2*dotProduct(laserdir,normal)*normal[1]]
print(reflection)
print(reflection[1]/reflection[0])
