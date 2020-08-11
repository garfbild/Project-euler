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

def primeFactors(n):
    primes = Sieve(n)
    dict = {}
    for p in primes:
        dict[p] = 0
        temp = n
        while temp > 0 and temp%p == 0:
            dict[p] += 1
            temp = temp / p
    return dict

for m in range(2,20):
    primeFactorsList = list(primeFactors(m).items())
    FactorsList = []
    for i in range(len(primeFactorsList)):
        if primeFactorsList[i][1] != 0:
            FactorsList = FactorsList + [primeFactorsList[i][0]]*primeFactorsList[i][1]

    for n in range(1,2**len(FactorsList)-1):
        heightFactors = []
        widthFactors = []
        for digit in str(bin(n))[2:].zfill(len(FactorsList)):
            if digit == "0":
                heightFactors.append(digit)
            else:
                widthFactors.append(digit)

    print()
