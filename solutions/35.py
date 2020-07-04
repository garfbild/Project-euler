def isPrime(n):
    if n%2 == 0 and n != 2:
        return False
    for d in range(3,int(n**0.5)+1):
        if n%d == 0:
            return False
    return True

saved = []
for n in range(2,1000000):
    strn = str(n)
    listn = list(strn)
    temp = listn
    if isPrime(n) == True:
        bol = True
        i= 0
        while i <= len(listn)-1 and bol == True:
            cir = []
            for j in range(len(temp)):
                cir.append(temp[j-1])
            if isPrime(int("".join(cir))) == False:
                bol = False
            temp = cir
            i+=1
        if bol == True:
            saved.append(int("".join(listn)))

print(len(saved))
