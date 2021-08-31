import copy
def extEuclid(a,b):
    if a < b:
        temp = a
        a = b
        b = temp
    r0,s0,t0 = a,1,0
    r1,s1,t1 = b,0,1
    while r1 != 0:
        q = int(r0/r1)
        #print(q," ",r0,s0,t0," ",r1,s1,t1)
        temp = [copy.deepcopy(r1),copy.deepcopy(s1),copy.deepcopy(t1)]
        r1 = r0 - q*r1
        s1 = s0 - q*s1
        t1 = t0 - q*t1
        #print(r1,s1,t1)
        r0,s0,t0 = temp[0],temp[1],temp[2]

    return r0,s0,t0

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

def phi(n):
    s = 1
    for d in range(2,n):
        if extEuclid(n,d)[0] == 1:
            s += 1
    return s

primes = Sieve(1000)
p = 1
i = 0
while p*primes[i] < 1000000:
    p = p *primes[i]
    i += 1
print(p)
for n in range(1,10):
    print(n,n/phi(n))
print(p/phi(p))
