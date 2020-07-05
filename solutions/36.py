def Binary(n):
    bin = []
    while n > 0:
        bin.append(str(n%2))
        n = int(n/2)
    return "".join(bin)

def isPal(n):
    strn = str(n)
    bol = True
    for i in range(int(len(strn)/2)):
        if strn[i] != strn[len(strn)-i-1]:
            bol = False
            break
    return bol

s = 0
for i in range(1,1000000):
    if isPal(i) == True and isPal(Binary(i)) == True:
        s += i


print(s)
