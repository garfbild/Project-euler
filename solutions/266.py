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

s = 1
for p in Sieve(190):
    s = s*p
print(s**0.5)
