import copy

def CountEmptyCells(Sudoku):
    emptyCells = 0
    for i in range(len(Sudoku)):
        for j in range(len(Sudoku)):
            if Sudoku[i][j] == 0:
                emptyCells += 1
    return emptyCells

def depthFirstSearch(Sudoku,y,x):
    print(CountEmptyCells(Sudoku))
    nextx = (x+1)%len(Sudoku)
    nexty = y
    if nextx == 0:
        nexty += 1
    if nexty == len(Sudoku):
        print(Sudoku)
        return Sudoku

    SudokuCopy = copy.deepcopy(Sudoku)

    if Sudoku[y][x] == 0:
        neighbours = []
        for n in range(len(Sudoku)):
            if Sudoku[y][n] != 0 and Sudoku[y][n] not in neighbours:
                neighbours.append(Sudoku[y][n])
            if Sudoku[n][x] != 0 and Sudoku[n][x] not in neighbours:
                neighbours.append(Sudoku[n][x])
        potentials = []
        for t in range(1,len(Sudoku)+1):
            if t not in neighbours:
                potentials.append(t)
        if len(potentials) == 0:
            return Sudoku
        SudokuCopy = copy.deepcopy(Sudoku)
        for p in potentials:
            SudokuCopy[y][x] = p
            Sudoku = depthFirstSearch(SudokuCopy,nexty,nextx)
            if CountEmptyCells(Sudoku) == 0:
                return Sudoku
    else:
         return depthFirstSearch(Sudoku,nexty,nextx)
    return SudokuCopy


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

smallSudoku = [[3,0,2,0],[0,0,0,0],[0,0,0,0],[0,1,0,4]]

[print(row) for row in newSudoku]
print()
print(depthFirstSearch(smallSudoku,0,0))
