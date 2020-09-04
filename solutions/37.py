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
s = 0
count = 0
for n in primes[4:]:
    print(n)
    if check(n,primes):
        s += n
        count += 1
    if count == 11:
        break

print(s)
# from sympy import primerange
#
# p = lambda x: list(primerange(x, x+10))
# A024770 = p(0)
# i=0
#
# while i<len(A024770):
#     print(A024770)
#     A024770+=p(A024770[i]*10)
#     i+=1
#
# print(A024770)
