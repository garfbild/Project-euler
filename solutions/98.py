file = open("solutions/words.txt","r")
strmatrix = file.read().split(",")
print(strmatrix)
dict = {}
for i in range(len(strmatrix)):
    try:
        dict[''.join(sorted(list(strmatrix[i][1:-1])))] += 1
    except:
        dict[''.join(sorted(list(strmatrix[i][1:-1])))] = 0
print(dict)
