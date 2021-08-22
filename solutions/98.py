#this is not good code
file = open("solutions/words.txt","r")
strmatrix = file.read().split(",")
#print(strmatrix)
dictana = {}
dictwor = {}
s = []
for i in range(len(strmatrix)):
    try:
        dictana[''.join(sorted(list(strmatrix[i][1:-1])))] += 1
        dictwor[''.join(sorted(list(strmatrix[i][1:-1])))].append(strmatrix[i][1:-1])
        s.append(''.join(sorted(list(strmatrix[i][1:-1]))))
    except:
        dictana[''.join(sorted(list(strmatrix[i][1:-1])))] = 0
        dictwor[''.join(sorted(list(strmatrix[i][1:-1])))] = [strmatrix[i][1:-1]]

for x in range(len(s)):
    for y in range(len(s)-1):
        if len(s[y]) < len(s[y+1]):
            temp = s[y]
            s[y] = s[y+1]
            s[y+1] = temp

print(s)
squares = []
for i in range(1,1000000):
    if len(str(i**2)) == 5:
        l = []
        bool = True
        for digit in str(i**2):
            if digit not in l:
                l.append(digit)
            else:
                bool = False
        if bool == True:
            print(i**2)
            squares.append(i**2)

words = dictwor[s[9]]
print(words)
for a in range(len(squares)-1,0,-1):
    n = squares[a]
    strn = str(n)
    dupe = list(words[1])
    for i in range(len(words[0])):
        for j in range(len(words[1])):
            if words[0][i] == words[1][j]:
                dupe[j] = strn[i]

    if int(''.join(dupe))**0.5 == int(int(''.join(dupe))**0.5):
        print(n,int(n)**0.5,''.join(dupe),int(''.join(dupe))**0.5)


    dupe = list(words[0])
    for i in range(len(words[1])):
        for j in range(len(words[0])):
            if words[0][j] == words[1][i]:
                dupe[j] = strn[i]
    if int(''.join(dupe))**0.5 == int(int(''.join(dupe))**0.5):
        print(n,int(n)**0.5,''.join(dupe),int(''.join(dupe))**0.5)
