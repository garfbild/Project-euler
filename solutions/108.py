#1/x + 1/y = 1/n
#x+y * n = xy
from decimal import *
from time import *

def Sieve(n):
    sieve = [0 for i in range(n+1)]
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

def intelligent(n):
    product = 1
    for i in primeFactors(n).values():
        product = product * (2*i + 1)
    return product

def dumb(n):
    total = 0
    for a in range(1,20*n):
        for b in range(1,n*20):
            if 1/a + 1/b == 1/n:
                total += 1
    return total
for n in range(1,10):
    print(intelligent(n),dumb(n))
    print()
