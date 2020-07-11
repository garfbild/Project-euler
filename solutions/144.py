import numpy as np
from numpy import linalg as LA

laserstart = np.array([0.0,10.1])
impact = np.array([1.4,-9.6])
laserdir = impact - laserstart

#create tangent vector
wallgradient = -4*impact[0]/impact[1]
wallVect = np.array([1,wallgradient])

#compute normalised normal
rotationMat = np.array([[0,-1],[1,0]])
normal = np.matmul(rotationMat, wallVect)
normNormal = normal / LA.norm(normal)

#compute reflection vector
reflection = laserdir - 2*np.dot(laserdir,normNormal)*normNormal
print(reflection)

#intersection
m = reflection[1]/reflection[0]
c = impact[1] - m * impact[0]

#y = mx + c substitute into x**2 + 4*Y**2
a1 = 4*m**2 + 1
a2 = 8*c*m
a3 = 4*c**2 - 100
print(a1,a2,a3)
print(np.roots([a1,a2,a3]))
