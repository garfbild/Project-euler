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
c = impact[1] - reflection[1]/reflection[0] * impact[0]
print(c)
