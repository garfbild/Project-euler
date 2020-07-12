import numpy as np
from numpy import linalg as LA
# 0 is x 1 is y

laseremit = np.array([0.0,10.1])
laserimpact = np.array([1.4,-9.6])

i = 0
bol = True
while bol:
    laserdir = laserimpact - laseremit
    #create tangent vector
    wallgradient = -4*laserimpact[0]/laserimpact[1]
    wallVect = np.array([1,wallgradient])

    #compute normalised normal
    rotationMat = np.array([[0,-1],[1,0]])
    normal = np.matmul(rotationMat, wallVect)
    normNormal = normal / LA.norm(normal)

    #compute reflection vector
    reflection = laserdir - 2*np.dot(laserdir,normNormal)*normNormal


    #intersection
    m = reflection[1]/reflection[0]
    c = laserimpact[1] - m * laserimpact[0]
    #y = mx + c substitute into 4x**2 + Y**2
    a1 = (m**2) + 4
    a2 = 2*c*m
    a3 = (c**2) - 100
    roots = np.roots([a1,a2,a3])

    if abs(roots[0]-laserimpact[0]) < 0.01:
        x = roots[1]
    else:
        x = roots[0]
    Lambda = (x - laserimpact[0])/reflection[0]
    y = reflection[1]*Lambda + laserimpact[1]


    laseremit = laserimpact
    laserimpact = np.array([x,y])

    if laserimpact[0] >= -0.01 and laserimpact[0] <= 0.01 and laserimpact[1] > 0:
        bol = False
    else:
        i += 1

print(i)
