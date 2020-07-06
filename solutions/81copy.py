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

n = 4
matrix = []
for x in range(n):
    temp = []
    for y in range(n):
        temp.append(random.randint(1,10))
    matrix.append(temp)
[print(row) for row in matrix]
print()
layer = [[n-1,n-1]]
for l in range(2*(n-1)):
    nextlayer = []
    for cell in layer:
        for adj in adjacents(cell):
            if adj not in nextlayer:
                nextlayer.append(adj)
    if len(layer) < len(nextlayer):
        constant = -1
    else:
        constant = 1

    for k in range(len(nextlayer)):
        if k + constant < 0:
            matrix[nextlayer[k][0]][nextlayer[k][1]] += matrix[layer[k][0]][layer[k][1]]
        elif k+constant < len(nextlayer):
            matrix[nextlayer[k][0]][nextlayer[k][1]] += matrix[layer[k+constant][0]][layer[k+constant][1]]
        elif matrix[layer[k+constant][0]][layer[k+constant][1]] < matrix[layer[k][0]][layer[k][1]]:
            matrix[nextlayer[k][0]][nextlayer[k][1]] += matrix[layer[k+constant][0]][layer[k+constant][1]]
        else:
            matrix[nextlayer[k][0]][nextlayer[k][1]] += matrix[layer[k][0]][layer[k][1]]


    layer = nextlayer
print(matrix[0][0])
