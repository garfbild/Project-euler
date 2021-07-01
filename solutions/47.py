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
    for p in primes:
        dict[p] = 0
        if n%p == 0:
            dict[p] += 1
            distinctFactors += 1
        if p > n:
            return dict
    return distinctFactors

primes = Sieve(10000000)
for i in range(647,1000):
    print(primeFactors(i,primes))
