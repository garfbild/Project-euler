import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def h(x,y):
    return ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * np.exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )

x_track = np.linspace(0,1600,3200)
y_track = np.linspace(0,1600,3200)
X, Y = np.meshgrid(x_track, y_track)

Z = h(X,Y)

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')

ax1.plot_surface(X, Y, Z, antialiased=True)
plt.show(block=True)

a = 1
x = 200
for i in range(100000):
    e1 = h(x,0)
    e2 = h(x+a,0)
    if e2/e1 > 1:
        x += a
    else:
        a = a/2

print(x,e1)
#
# a = 1
# x = 200
# for i in range(100000):
#     e1 = h(x,1600)
#     e2 = h(x+a,1600)
#     if e2/e1 > 1:
#         x += a
#     else:
#         a = a/2
#
# print(x,e1)
#
# a = 1
# y = 200
# for i in range(100000):
#     e1 = h(0,y)
#     e2 = h(0,y+a)
#     if e2/e1 > 1:
#         y += a
#     else:
#         a = a/2
#
# print(y,e1)
#
# a = 1
# y = 200
# for i in range(100000):
#     e1 = h(1600,y)
#     e2 = h(1600,y+a)
#     if e2/e1 > 1:
#         y += a
#     else:
#         a = a/2
#
# print(y,e1)

# 895.5000000002328 10396.462189127302 x = 0
# 667.0000000000036 9571.536994105089 x = 1600
# 895.5000000002328 10396.462189127302 y = 0
# 667.0000000000036 9571.536994105089 y = 1600

fmin = 10396.462189127302

plt.contour((Z),[fmin])
plt.show()
