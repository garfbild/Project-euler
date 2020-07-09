import random
import copy

file = open("solutions/matrix.txt","r")
strmatrix = [row.split(",") for row in file.read().split('\n')]
matrix = []
n = 80
for x in range(n):
    temp = []
    for y in range(n):
        temp.append(int(strmatrix[x][y]))
    matrix.append(temp)

for i in range(n-2,-1,-1):
    temp = copy.deepcopy(matrix)
    for j in range(n):
        min = int(matrix[j][i+1])

        top = 0
        row = j
        while row - 1 >= 0:
            top += matrix[row-1][i]
            if top + matrix[row-1][i+1] < min:
                min = top + matrix[row-1][i+1]
            row = row - 1

        bottom = 0
        row = j
        while row + 1 <= n - 1:
            bottom += matrix[row+1][i]
            if bottom + matrix[row+1][i+1] < min:
                min = bottom + matrix[row+1][i+1]
            row = row + 1
        temp[j][i] += min

    matrix = temp


min = matrix[i][0]
for i in range(n):
    if matrix[i][0] < min:
        min = matrix[i][0]
print(min)
