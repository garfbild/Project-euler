def isPrime(n):
    if n%2 == 0 and n != 2:
        return False
    for d in range(3,int(n**0.5)+1):
        if n%d == 0:
            return False
    return True

primes = 3
n = 1
while primes/(4*n + 1) >= 0.1 :
    n+=1
    d = (2*n + 1)**2
    for i in range(1,4):
        if isPrime(d-(i*2*n)):
            primes+=1
print(d,2*n + 1,4*n+1,primes,primes/(4*n + 1))
