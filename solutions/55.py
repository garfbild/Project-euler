def isPal(n):
    strn = str(n)
    bol = True
    for i in range(int(len(strn)/2)):
        if strn[i] != strn[len(strn)-i-1]:
            bol = False
            break
    return bol

def lychel(n):
    temp = n
    for i in range(51):
        strn = str(temp)
        reverse = strn[::-1]
        temp = temp+int(reverse)
        if isPal(temp):
            return False
    return True

s = 0
for i in range(0,10000):
    if lychel(i):
        s += 1
print(s)
