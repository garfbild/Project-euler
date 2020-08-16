# https://oeis.org/search?q=2%2C3%2C3%2C6%2C6%2C10%2C14&language=english&go=Search
global primes
primes = [2]

def Sieve(n):
    global primes

    for p in primes:
        if n%p == 0:
            return False
    primes.append(n)
    return True

s = 0
M = 0
# while s < 2000:
#     M += 1
#     while Sieve(M):
#         M += 1
#     temp = 0
#     for b in range(1,M+1):
#         for a in range(1,b+1):
#             if (((a+b)**2 + M**2)**0.5).is_integer():
#                 temp += 1
#     s += temp

target = 1
while s < 1000000:
    if s > target * 10000:
        print(target,s)
        target += 1
    M += 1
    while Sieve(M):
        M += 1
    temp = 0
    for n in range(2,2*M):
        if (((n)**2 + M**2)**0.5).is_integer():
            if n > M:
                temp += int(n/2)+ (M-n+1)
            else:
                temp += int(n/2)
    s += temp

print(M,s)
