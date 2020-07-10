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
a = reflection[0]**2 * 4*reflection[1]**2
b = 2 * impact[0] * reflection[0] + 4 * impact[1] * reflection[1]
c = impact[0]**2 + 4 * impact[1] - 100
print(a,b,c)
Lambda = np.roots([a,b,c])
print(reflection * Lambda[1] + impact)
print(reflection * Lambda[0] + impact)
