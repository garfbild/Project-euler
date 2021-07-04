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

def isPrime(n):
    if n%2 == 0 and n != 2:
        return False
    for d in range(3,int(n**0.5)+1):
        if n%d == 0:
            return False
    return True

primes = Sieve(1000000)
s = 0
i = 0
while s+primes[i] < 1000000:
    if isPrime(s):
        print(s)
    s += primes[i]
    i += 1

print(s)
print(i,primes[i])
#print(primes)

for i in range(len(primes)):
    s += -primes[i]
    if isPrime(s):
        print(s)
