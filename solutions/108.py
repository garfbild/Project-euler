#solutions to 1/x + 1/y = 1/n
# X= x-n Y = y-n solving number of solutions X*Y = n**2
# divisors of n**2
#https://oeis.org/A048691
from sympy import divisor_count
import random
import time
import copy
global SieveObj

class Sieve:
    def __init__(self,n):
        self._n = n
        sieve = [0]*(n+1)
        sieve[0],sieve[1] = 1,1
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

        self._Sieve = sieve
        self._Primes = primes

    def getPrimes(self,n):
        if n <= self._n:
            return [i for i in self._Primes if i <= n]
        else:
            sieve = self._Sieve + [0]*(n-self._n)
            for p in self._Primes:
                s = self._n - self._n%p
                while s + p <= n:
                    s += p
                    sieve[s] = 1
            for d in range(int(self._n**0.5),int(n**0.5)+1):
                if sieve[d] == 0:
                    s = d
                    while s + d <= n:
                        s += d
                        sieve[s] = 1
        primes = self._Primes
        for i in range(self._n,len(sieve)):
            if sieve[i] == 0:
                primes.append(i)

        self._Sieve = sieve
        self._Primes = primes
        return self._Primes


def tau(n):
    global SieveObj
    primes = SieveObj.getPrimes(n)
    exponents =[]
    primeCount = []
    for p in primes:
        num = n
        temp = 0
        while num%p == 0:
            primeCount.append(p)
            temp += 1
            num = num/p
        exponents.append(temp)
    a = 1
    print(exponents)
    print(primeCount)
    for e in exponents:
        a = a*(e+1)
    return a

# for i in range(8):
#     x = random.randint(10**i, 10**(i+1))
#     start = time.time()
#     tau(x)
#     end = time.time()
#     print(start-end,end = ' ')
#     start = time.time()
#     divisor_count(x)
#     end = time.time()
#     print(start-end)
#
#
# n = Mul(*[i for i in range(5)])
# print(n)


# n = 1
# print((tau(1260**2)+1)/2)
# while int((tau(n**2)+1)/2) < 1000:
#     n += 1
# print(n)

# n = 1
# while int((divisor_count(n**2)+1)/2) < 1000:
#     n += 1
# print(n)
#180180
global m
m = 9999999999999999999999999999999

def Product(primes,exponents):
    s = 1
    for i in range(len(primes)):
        s = s*primes[i]**exponents[i]
    return s

SieveObj = Sieve (100000)
primes = SieveObj.getPrimes(100000)
def Search(depth,primes,exponents):
    global m
    e = copy.deepcopy(exponents)
    s = Product(primes,e)
    if int((divisor_count(s**2)+1)/2) >= 1000:
        if s < m:
            m = s
            print(e)
        return
    for i in range(1,e[depth-1]+1):
        e[depth] = i
        Search(depth+1,primes,e)



for i in range(1,4):
    exponents = [0]*len(primes)
    exponents[0] = i
    exponents = Search(1,primes,exponents)
print(m)
