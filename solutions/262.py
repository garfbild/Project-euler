import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def h(x,y):
    return ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * np.exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )

x_track = np.linspace(0,1600,1600)
y_track = np.linspace(0,1600,1600)
X, Y = np.meshgrid(x_track, y_track)
print(X.shape)
print(Y.shape)

terrain = np.array([])
for x in x_track:
    temp = []
    for y in y_track:
        temp.append(h(x,y))
    terrain.append(temp)

print(len(terrain),len(terrain[0]))

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(X.flatten(), Y.flatten(), terrain.flatten(), zdir='z')
plt.show()
