file = open("solutions/sudoku.txt","r")
List = file.read().split('\n')

g = 0
old_sudoku = List[10*g + 1:10*(g+1)]
new_sudoku = []
for i in range(9):
    old_row = list(old_sudoku[i])
    new_row = []
    for j in range(9):
        new_row.append(int(old_row[j]))
    print(new_row)
    new_sudoku.append(new_row)
print()
potentials = []
for p in range(9):
    row = []
    for q in range(9):
        row.append([])
    potentials.append(row)

for y in range(9):
    for x in range(9):
        for n in range(9):
            if new_sudoku[y][n] != 0 and new_sudoku[y][n] not in potentials[y][x]:
                potentials[y][x].append(new_sudoku[y][n])
            if new_sudoku[n][x] != 0 and new_sudoku[n][x] not in potentials[y][x]:
                potentials[y][x].append(new_sudoku[n][x])
        if new_sudoku[y][x] == 0:
            temp = []
            for m in range(1,10):
                if m not in potentials[y][x]:
                    temp.append(m)
            potentials[y][x] = temp
            if len(temp) == 1:
                print(temp,y,x)

for row in potentials:
    print(row)
