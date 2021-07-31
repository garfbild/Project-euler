#solutions to 1/x + 1/y = 1/n
# X= x-n Y = y-n solving number of solutions X*Y = n**2
# divisors of n**2
#https://oeis.org/A048691
from sympy import divisor_count
import random
import time

import module
import inspect
src = inspect.getsource(module)

print(src)

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

def tau(n):
    primes = Sieve(n)
    exponents =[]
    for p in primes:
        num = n
        temp = 0
        while num%p == 0:
            temp += 1
            num = num/p
        exponents.append(temp)

    a = 1
    for e in exponents:
        a = a*(e+1)
    return(a)

for i in range(8):
    x = random.randint(10**i, 10**(i+1))
    start = time.time()
    tau(x)
    end = time.time()
    print(start-end,end = ' ')
    start = time.time()
    divisor_count(x)
    end = time.time()
    print(start-end)


n = 1
# while int((divisor_count(n**2)+1)/2) < 1000:
#     n += 1
# print(n)
