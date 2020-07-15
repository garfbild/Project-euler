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

s = 1
primes = Sieve(190)
for p in primes:
    s = s*p

print(len(primes))
print(s)
SR = s**0.5
print(SR)

t = 1
i = 0
while t*primes[i] < SR:
    t = t*primes[i]
    i += 1
print(t)
print(SR-t)
