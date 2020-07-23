file = open("solutions/sudoku.txt","r")
List = file.read().split('\n')
potentials = [[[]]*9]*9
for row in potentials:
    print(row)
for g in range(50):
    Sudoku = List[10*g + 1:10*(g+1)]
