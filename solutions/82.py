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

n = 3
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
        print(target,":")
        min = matrix[j][i+1]

        top = 0
        row = j
        while row - 1 >= 0:
            print(matrix[row-1][i])
            top += matrix[row-1][i]
            if top + matrix[row-1][i+1] < min:
                min = top + matrix[row-1][i+1]
            row = row - 1

        bottom = 0
        row = j
        while row + 1 <= n - 1:
            bottom += matrix[row+1][i]
            if top + matrix[row+1][i+1] < min:
                min = top + matrix[row+1][i+1]
            row = row + 1
        temp[j][i] += min


[print(row) for row in matrix]
