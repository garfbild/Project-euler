import copy
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

def extEuclid(a,b):
    if a < b:
        temp = a
        a = b
        b = temp
    r0,s0,t0 = a,1,0
    r1,s1,t1 = b,0,1
    while r1 != 0:
        q = int(r0/r1)
        temp = [copy.deepcopy(r1),copy.deepcopy(s1),copy.deepcopy(t1)]
        r1 = r0 - q*r1
        s1 = s0 - q*s1
        t1 = t0 - q*t1
        r0,s0,t0 = temp[0],temp[1],temp[2]
    return r0,s0,t0


primes = Sieve(1000003)
print(len(primes))
S = 0
for x in range(2,len(primes)-1):
    p1 = primes[x]
    p2 = primes[x+1]
    prefix = 1
    power = len(str(p1))
    r,s,t = extEuclid(p2,10**power)
    if s*10**power + t*p2 == 1:
        #chinese remainder
        S += p1*t*p2 %(p2*(10**power))
    else:
        S += p1*s*p2 %(p2*(10**power))

print(S)
