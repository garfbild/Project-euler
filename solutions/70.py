import time
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

def tau(n,primes):
    i = 0
    t = n
    while primes[i] < n:
        if n%primes[i] == 0:
            t = t*((primes[i]-1)/primes[i])
            n = n/primes[i]
        i += 1
    return int(t)

def isPerm(m,n):
    strM = [*str(m)]
    strN = [*str(n)]
    if len(strM) != len(strN):
        return False
    for i in range(len(strM)):
        var = True
        j = 0
        while var == True and j < len(strN):
            if strM[i] == strN[j]:
                var = False
                strN[j] = "A"
            j += 1
        if var == True:
            return False
    if strN == ["A"]*len(strN):
        return True
m = 10**7
print(isPerm(123,321))
t1 = time.time()
primes = Sieve(m)
t2 = time.time()
print("primes",t2-t1)
min = 9999999999999999
minI = 0
tauTime = 0
permTime = 0
for i in (num for num in range(1,1000) if num not in primes):
    t1 = time.time()
    j = tau(i,primes)
    t2 = time.time()
    tauTime += (t2-t1)
    t1 = time.time()
    if isPerm(i,j):
        print(i,j)
        if i/j < min:
            minI = i
    t2 = time.time()
    permTime += (t2-t1)

print(minI)
print("perm",permTime)
print("tau",tauTime)
