file = open("solutions/keylog.txt","r")
List = file.read().split('\n')
List = List[:-1]
List = list(set(List))
print(List)

digits = set()
for x in List:
    for y in x:
        if x not in digits:
            digits.add(y)
print(digits)

myDict = {}
for x in digits:
    myDict[x] = set()
    for y in List:
        if x in y:
            if y[1] == x:
                myDict[x].add(y[0])
            elif y[2] == x:
                myDict[x].add(y[0])
                myDict[x].add(y[1])

print(myDict)
Number = []
for i in range(len(digits)):
    for j in digits:
        if len(myDict[j]) == i:
            Number.append(j)
print(Number)
