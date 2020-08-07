import copy

def CountEmptyCells(Sudoku):
    emptyCells = 0
    for i in range(len(Sudoku)):
        for j in range(len(Sudoku)):
            if Sudoku[i][j] == 0:
                emptyCells += 1
    return emptyCells

def FindPotentials(Sudoku,y,x):
    neighbours = []
    for n in range(len(Sudoku)):
        if Sudoku[y][n] != 0 and Sudoku[y][n] not in neighbours:
            neighbours.append(Sudoku[y][n])
        if Sudoku[n][x] != 0 and Sudoku[n][x] not in neighbours:
            neighbours.append(Sudoku[n][x])

    for i in range((x - x%3),(x - x%3)+3):
        for j in range((y - y%3),(y - y%3)+3):
            if Sudoku[j][i] != 0 and Sudoku[j][i] not in neighbours:
                neighbours.append(Sudoku[j][i])

    potentials = []
    for t in range(1,len(Sudoku)+1):
        if t not in neighbours:
            potentials.append(t)

    return potentials

def depthFirstSearch(Sudoku,y,x):
    nextx = (x+1)%len(Sudoku)
    nexty = y
    if nextx == 0:
        nexty += 1
    if y == len(Sudoku):
        [print(row) for row in Sudoku]
        print()
        return Sudoku

    if Sudoku[y][x] == 0:
        potentials = FindPotentials(Sudoku,y,x)
        if len(potentials) == 0:
            return Sudoku

        for p in potentials:
            Sudoku[y][x] = p
            tempSudoku = depthFirstSearch(Sudoku,nexty,nextx)
            if CountEmptyCells(tempSudoku) == 0:
                return tempSudoku
            Sudoku[y][x] = 0
    else:
         return depthFirstSearch(Sudoku,nexty,nextx)
    return Sudoku


file = open("solutions/sudoku.txt","r")
List = file.read().split('\n')

S = 0
for g in range(50):
    oldSudoku = List[10*g + 1:10*(g+1)]
    newSudoku = []
    for i in range(9):
        oldRow = list(oldSudoku[i])
        newRow = []
        for j in range(9):
            newRow.append(int(oldRow[j]))
        newSudoku.append(newRow)
    SolvedSudoku = depthFirstSearch(newSudoku,0,0)
    S += SolvedSudoku[0][0]*100 + SolvedSudoku[0][1]*10 + SolvedSudoku[0][2]

print(S)
