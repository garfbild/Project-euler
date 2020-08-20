from functools import reduce
from sympy import divisor_count


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

primes = Sieve(1000)

k = 0
while 3**k < 8000000:
    k += 1
print(k,3**k)

n = reduce(lambda x, y: x*y,primes[0:k])
print(n)
print((divisor_count(n**2)+1)/2)
# seems like this solution model would work but I dont know how I would go about minimising n and (tau(n**2)+1)/2 simultaneously
