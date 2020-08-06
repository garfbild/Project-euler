import copy

def CountEmptyCells(Sudoku):
    emptyCells = 0
    for i in range(9):
        for j in range(9):
            if Sudoku[i][j] == 0:
                emptyCells += 1
    return emptyCells

def depthFirstSearch(Sudoku,y,x):
    nextx = (x+1)%9
    nexty = y
    if nextx == 0:
        nexty += 1
    if nexty == 9:
        return

    SudokuCopy = copy.deepcopy(Sudoku)

    if Sudoku[y][x] == 0:
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
        print(y,x,potentials)
        print()
        if len(potentials) == 0:
            return
        SudokuCopy = copy.deepcopy(Sudoku)
        for p in potentials:
            SudokuCopy[y][x] = p
            depthFirstSearch(SudokuCopy,nexty,nextx)
    else:
        print(y,x,"static")
        print()
        depthFirstSearch(Sudoku,nexty,nextx)


file = open("solutions/sudoku.txt","r")
List = file.read().split('\n')

g = 0
oldSudoku = List[10*g + 1:10*(g+1)]
newSudoku = []
for i in range(9):
    oldRow = list(oldSudoku[i])
    newRow = []
    for j in range(9):
        newRow.append(int(oldRow[j]))
    newSudoku.append(newRow)


[print(row) for row in newSudoku]
print()
depthFirstSearch(newSudoku,0,0)
