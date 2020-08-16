import time

global primes
global seive
primes = [2]
sieve = []

def Sieve(n):
    global primes

    for p in primes:
        if n%p == 0:
            return False
    primes.append(n)
    return True


#lengths a,b,c a>b>c

s = 0
M = 1
while s < 1000000:
    for b in range(1,M+1):
        for a in range(1,b+1):
            if (((a+b)**2 + M**2)**0.5).is_integer():
                s += 1

    M += 1
    while Sieve(M):
        M += 1

print(s)
