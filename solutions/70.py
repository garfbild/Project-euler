import time
def Sieve(n):
    sieve = [0] * int(n+1)
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

def phi(n,primes):
    i = 0
    t = n
    while primes[i] <= n:
        if n%primes[i] == 0:
            t = t*((primes[i]-1)/primes[i])
            while n%primes[i] == 0:
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
    return True

m = 10**7
primes = Sieve(m/2)#only looked at products of two primes

minV = 9999999999999999
minN = 0
p = len(primes)-1
while p >= 0:
    q = 0
    f1 = primes[p]
    f2 = primes[q]
    #using eulers product formula it was clear that smallest value was when n was a prime, however, the totient could never permute. Therefore searched all products of two primes. powers have no effect on ratio.
    n = f1*f2
    while q < p and n < m:
        f2 = primes[q]
        n = f1*f2
        phiV = (f1-1)*(f2-1)
        if n/phiV < minV:
            # isPerm is a time costly function
            if isPerm(n,phiV):
                print(n,phiV,n/phiV,f1,f2)
                minV = n/phiV
                minN = n
        q += 1
    p += -1

#brute force
# for i in (num for num in range(2,10000) if num not in primes):
#     j = phi(i,primes)
#     if isPerm(i,j):
#         print(i,j)
#         if i/j < min:
#             minV = i/j
#             min = i

print(minV,minN)
