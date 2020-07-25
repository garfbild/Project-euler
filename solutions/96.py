file = open("solutions/sudoku.txt","r")
List = file.read().split('\n')

g = 0
old_sudoku = List[10*g + 1:10*(g+1)]
new_sudoku = []
empty_calls = 0
for i in range(9):
    old_row = list(old_sudoku[i])
    new_row = []
    for j in range(9):
        new_row.append(int(old_row[j]))
        if int(old_row[j]) == 0:
            empty_cells += 1
    print(new_row)
    new_sudoku.append(new_row)
print()

for y in range(9):
    for x in range(9):
        neighbours = []
        for n in range(9):
            if new_sudoku[y][n] != 0 and new_sudoku[y][n] not in neighbours:
                neighbours.append(new_sudoku[y][n])
            if new_sudoku[n][x] != 0 and new_sudoku[n][x] not in neighbours:
                neighbours.append(new_sudoku[n][x])
        if new_sudoku[y][x] == 0:
            temp = []
            for m in range(1,10):
                if m not in neighbours:
                    temp.append(m)
            if len(temp) == 1:
                new_sudoku[y][x] = temp[0]
