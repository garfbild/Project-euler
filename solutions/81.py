import random
import time

def adjacents(pos):
    ads = []
    if pos[0] - 1 >= 0:
        ads.append([pos[0]-1,pos[1]])
    if pos[1] - 1 >= 0:
        ads.append([pos[0],pos[1]-1])
    return ads

file = open("solutions/matrix.txt","r")
strmatrix = [row.split(",") for row in file.read().split('\n')]
matrix = []
n = 80
for x in range(n):
    temp = []
    for y in range(n):
        temp.append(int(strmatrix[x][y]))
    matrix.append(temp)


for j in range(n-1,0,-1):
    matrix[n-1][j-1] += matrix[n-1][j]
    matrix[j-1][n-1] += matrix[j][n-1]

layer = [[n-2,n-2]]
for l in range(2*(n-2)+1):
    nextlayer = []
    for cell in layer:
        if matrix[cell[0]+1][cell[1]] < matrix[cell[0]][cell[1]+1]:
            matrix[cell[0]][cell[1]] += matrix[cell[0]+1][cell[1]]
        else:
            matrix[cell[0]][cell[1]] += matrix[cell[0]][cell[1]+1]
        for adj in adjacents(cell):
            if adj not in nextlayer:
                nextlayer.append(adj)
    layer = nextlayer


[print(row) for row in matrix]
print()
