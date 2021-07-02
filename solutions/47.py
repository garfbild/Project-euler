def Sieve(n):
    sieve = [0] * (n+1)
    for d in range(2,int(n**0.5)+1):
        if sieve[d] == 0:
            s = d
            while s + d <= n:
                s += d
                sieve[s] = 1

    primes = []
    for i in range(len(sieve)):
        if sieve[i] == 0:
            primes.append(i)
    return primes[2:]

def primeFactors(n,p):
    primes = p
    dict = {}
    distinctFactors = 0
    temp = n
    for p in primes:
        dict[p] = 0
        boolvar = False
        while temp%p == 0:
            temp = temp/p
            dict[p] += 1
            boolvar = True
        if boolvar == True:
            distinctFactors += 1
        if p > n:
            return distinctFactors,dict
    return distinctFactors,dict

def checkDistinct(a,b):
    #a should be shorter
    for key in list(a.keys()):
        if a[key] == b[key] and a[key] != 0:
            return False
    return True

n = 10000
primes = Sieve(n)
consolidation = []

for i in range(1,n):
    a = primeFactors(i,primes)
    if a[0] == 4:
        #print(i)
        b = primeFactors(i+1,primes)
        if b[0] == 4:
            print(i,i+1)
            c = primeFactors(i+2,primes)
            if c[0] == 4:
                print(i,i+1,i+2)
                d = primeFactors(i+3,primes)
                if d[0] == 4:
                    print(i,a,b,c)
