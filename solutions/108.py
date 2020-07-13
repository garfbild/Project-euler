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

def intelligent(n):
    total = 0
    for i in primeFactors(n).values():
        total += (2*i) + 1
    print(total/2)

def dumb(n):
    total = 0
    for a in range(1,2*n + 1):
        for b in range(2*n,(n+1)*10):
            if 1/a + 1/b == 1/n:
                total += 1
    return total

n = 1
while dumb(n) < 1000:
    if n % 10 == 0:
        print(n)
    n += 1

print(n)
