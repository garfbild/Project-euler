import copy

def CountEmptyCells(Sudoku):
    empty_cells = 0
    for i in range(9):
        for j in range(9):
            if Sudoku[i][j] == 0:
                empty_cells += 1
    return empty_cells

def depthFirstSearch(Sudoku,y,x):
    [print(row) for row in new_sudoku]
    print()
    if CountEmptyCells(Sudoku) == 0:
        return
    nextx = x+1 % 8
    nexty = y+1
    if nexty == 9:
        return Sudoku

    neighbours = []
    for n in range(9):
        if Sudoku[y][n] != 0 and Sudoku[y][n] not in neighbours:
            neighbours.append(Sudoku[y][n])
        if Sudoku[n][x] != 0 and Sudoku[n][x] not in neighbours:
            neighbours.append(Sudoku[n][x])
    potentials = []
    for t in range(1,9):
        if t not in neighbours:
            potentials.append(t)

    tempSudoku = copy.deepcopy(Sudoku)
    for p in range(len(potentials)):
        tempSudoku[nexty][nextx] = potentials[p]
        Suduko = depthFirstSearch(tempSudoku,nexty,nexty)
        if CountEmptyCells(Sudoku) == 0:
            return Sudoku

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
    new_sudoku.append(new_row)


[print(row) for row in new_sudoku]
print(depthFirstSearch(new_sudoku,0,0))
