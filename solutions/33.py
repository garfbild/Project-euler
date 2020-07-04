def isPrime(n):
    if n%2 == 0 and n != 2:
        return False
    for d in range(3,int(n**0.5)+1):
        if n%d == 0:
            return False
    return True

def divisors(n):
    divisorlist = []
    if n < 0:
        n = -n
    for d in range(2,int(n)+1):
        if n%d == 0 and isPrime(d) == True:
            temp = n
            while temp %d == 0:
                divisorlist.append(d)
                temp = temp / d

    return divisorlist

saved = []
for a in range(11,100):
    for b in range(a+1,100):
        for c in range(len(str(a))):
            for d in range(len(str(b))):
                if str(a)[c] == str(b)[d] and str(a)[c] != "0":
                    newa = list(str(a))
                    newb = list(str(b))
                    del newa[c]
                    del newb[d]
                    if [newa,newb] not in saved:
                        saved.append([a,b,int(newa[0]),int(newb[0])])
solved = []
print(saved)
for e in saved:
    if e[2] != 0 and e[3] != 0:
        if e[0]/e[1] == e[2]/e[3]:
            print(e)
