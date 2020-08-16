# https://oeis.org/search?q=2%2C3%2C3%2C6%2C6%2C10%2C14&language=english&go=Search
global primes
primes = [2]

def Sieve(n):
    global primes

    for p in primes:
        if n%p == 0:
            return False
    primes.append(n)
    return True

s = 0
M = 0
while s < 100:
    M += 1
    while Sieve(M):
        M += 1

    for b in range(1,M+1):
        for a in range(1,b+1):
            print(a+b)
            if (((a+b)**2 + M**2)**0.5).is_integer():
                s += 1

print(M,s)
