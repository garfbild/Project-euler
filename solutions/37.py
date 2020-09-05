def check(n,primes):
    digits = len(str(n))
    for j in range(digits-1,-1,-1):
        if n//10**j not in primes:
            return False
    for i in range(1,digits+1):
        if n%10**i not in primes:
            return False
    return True

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

primes = Sieve(10**8)

rightTruncatable = primes[:4]
i = 0
while i < len(rightTruncatable):
    for n in range(1,10,2):
        if rightTruncatable[i]*10 + n in primes:
            rightTruncatable.append(rightTruncatable[i]*10 + n)
    i+=1

print(rightTruncatable)
