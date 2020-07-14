import time
import numpy as np

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

def GCD(a,b):
    #a > b
    if a == b:
        return a
    elif a < b:
        temp = a
        a = b
        b = temp

    if a%b == 0:
        return b

    r = -1
    while a%b != 0:
        r = a%b
        a = b
        b = r
    return r

def dumb():
    # just for 1
    s = 0
    x = 1
    y = x + 1
    z = (x**2 + y**2)**0.5
    while x + y + z < 100000000:
        x += 1
        y = x + 1
        c = (x**2 + (x+1)**2)**0.5
        if c == int(c):
            print(x,y,c)
            s += 1
    print(s)

def lessdumb():
    saved = []
    for z in range(5,10**4):
        mul = [0] * z
        for n in range(1,z-1):
            if mul[n] == 0:
                if z%n == 0:
                    roots = np.roots([2,2*n,n**2 - z**2])
                    x = sorted(roots)[1]
                    if x.is_integer() == True:
                        saved.append([x,x+n,z])
                else:
                    d = n
                    while d < z:
                        mul[d] = 1
                        d += n


#while 2 m**2 + 2m*n < 10**8
t = time.time()
s = 0
for n in range(1,5000):
    #if n is odd then m must be even
    if n%2 == 1:
        const = 2
    else:
        const = 1
    m = n+1
    while 2*m**2 + 2*m*n <= 10**8:
        if m%2 != 1 or n%2 != 1:
            if GCD(m,n) == 1:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                s += 1
        m+=const

print(time.time()-t)
print(s)
