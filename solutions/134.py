#not finised
def Sieve(n):
    sieve = [0] * (n+1)
    for d in range(2,int(n**0.5)):
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

primes = Sieve(1000000)
print(len(primes))
S = 0
for x in range(10):
    if x%100 == 0:
        print(x)
    if x != 1:
        p1 = primes[x]
        p2 = primes[x+1]
        prefix = 1
        power = len(str(p1))
        while (prefix*(10**power) + p1) % p2 != 0:
            prefix += 1
        print(p1,p2,prefix*(10**power) + p1)
        S += prefix*100 + p1
print(S)
