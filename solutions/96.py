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


[print(row) for row in new_sudoku]
print(empty_cells)
print()

while empty_cells > 0:
