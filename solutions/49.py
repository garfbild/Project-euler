import time
def Sieve(n):
    sieve = [0] * (n+1)
    primes = []
    for d in range(2,int(n**0.5)+1):
        if sieve[d] == 0:
            s = d
            primes.append(d)
            while s + d <= n:
                s += d
                sieve[s] = 1

    for i in range(int(n**0.5),len(sieve)):
        if sieve[i] == 0:
            primes.append(i)
    return primes

primes = Sieve(10000)
primes = [i for i in primes if i > 1000]
print(primes)
for i in primes:
    # stri = str(i)
    # head = stri[0:3]
    # headspin = int(head[1:] + head[0] + stri[3])
    # headspinn = int(head[-1] + head[:-1] + stri[3])
    # if headspin in primes and headspinn in primes:
    #     print(i,headspin,headspinn)
    if i + 3330 in primes and i + 6660 in primes:
        if sorted(list(str(i))) == sorted(list(str(i+3330))) and sorted(list(str(i+6660))) == sorted(list(str(i+3330))):
            print(i,i+3330,i+6660)
