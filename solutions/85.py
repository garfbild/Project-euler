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

def primeFactors(n):
    primes = Sieve(n)
    dict = {}
    for p in primes:
        dict[p] = 0
        temp = n
        while temp > 0 and temp%p == 0:
            dict[p] += 1
            temp = temp / p
    return dict

for m in range(2,10):
    primeFactorsList = list(primeFactors(m).items())
    s = 0
    for i in range(len(primeFactorsList)):
        s += primeFactorsList[i][1]
    print(m,s)

width = 4
height = 1
s = 0
for x in range(1,width+1):
    for y in range(1,height+1):
        s += (width-x+1)*(height-y+1)
print(s)
