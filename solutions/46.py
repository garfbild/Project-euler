def isPrime(n):
    if n%2 == 0 and n != 2:
        return False
    for d in range(3,int(n**0.5)+1):
        if n%d == 0:
            return False
    return True

primes = []
for n in range(3,10000,2):
    if isPrime(n) == False:
        s = 1
        bol = False
        while 2*s**2 < n and bol == False :
            for p in range(2,n):
                if p not in primes:
                    if isPrime(p) == True:
                        primes.append(p)
                        if 2*s**2 + p == n:
                            bol = True
                else:
                    if 2*s**2 + p == n:
                        bol = True
            s +=1
        if bol == False:
            print(n)
