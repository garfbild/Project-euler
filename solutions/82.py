import random

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

for i in range(n-2,-1,-1):
    temp = matrix
    for j in range(n):
        target = matrix[j][i]
        for k in range(n):

        print()
