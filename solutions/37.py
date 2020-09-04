def check(n,primes):
    digits = len(str(n))
    for i in range(1,digits+1):
        if n%10**i not in primes:
            return False
    for j in range(digits-1,-1,-1):
        if n//10**j not in primes:
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

primes = Sieve(10**7)
s = 0
count = 0
for n in primes[4:]:
    if check(n,primes):
        s += n
        count += 1
        print(n)
    if count == 11:
        break
print(s)
