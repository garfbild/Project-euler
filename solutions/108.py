#1/x + 1/y = 1/n
#x+y * n = xy
from decimal import *
from time import *

def Sieve(n):
    sieve = [0 for i in range(n+1)]
    for d in range(2,int(n**0.5)+1):
        if sieve[d] == 0:
            s = d
            while s + d <= n+1:
                s += d
                sieve[s] = 1

    primes = []
    for i in range(len(sieve)):
        if sieve[i] == 0:
            primes.append(i)
    return primes[2:]

def primeFactors(n):
    t = time()
    primes = Sieve(n)
    dict = {}
    for p in primes:
        dict[p] = 0
        temp = n
        while temp > 0 and temp%p == 0:
            dict[p] += 1
            temp = temp / p
    return dict

n = 4
total = 0
for i in primeFactors(n).values():
    total += (2*i) + 1
print(total)
