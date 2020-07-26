file = open("solutions/sudoku.txt","r")
List = file.read().split('\n')

g = 0
old_sudoku = List[10*g + 1:10*(g+1)]
new_sudoku = []
empty_cells = 0
for i in range(9):
    old_row = list(old_sudoku[i])
    new_row = []
    for j in range(9):
        new_row.append(int(old_row[j]))
        if int(old_row[j]) == 0:
            empty_cells += 1
    new_sudoku.append(new_row)

for k in range(15):
    [print(row) for row in new_sudoku]
    print(empty_cells)
    print()
    y = 0
    while y <= 8:
        x=0
        while x <= 8:
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
                    empty_cells += -1
                    print(x+1,y+1)
                    x,y = 9,9
            x+=1
        y+=1
print(new_sudoku)
