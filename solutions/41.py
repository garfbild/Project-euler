import copy

def prevLexicographicPermutation(a):
    n = len(a)
    k_copy = -1
    for k in range(n-2,-1,-1):
        if a[k] > a[k+1]:
            k_copy = int(k)
            break
    if k_copy == -1:
        return a
    for l in range(n-1,k_copy-1,-1):
        if a[k_copy] > a[l]:
            l_copy = int(l)
            break
    temp = a[k_copy]
    a[k_copy] = a[l_copy]
    a[l_copy] = temp

    return a[:k_copy+1] + a[k_copy+1:][::-1]

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

def Integerise(a):
    i = 0
    n = len(a)
    for x in range(n):
        i += a[x]*10**(n-x-1)
    return i

def Factorial(n):
    if n == 1:
        return n
    else:
        return n*Factorial(n-1)

def isPrime(n):
    if n%2 == 0 and n != 2:
        return False
    for d in range(3,int(n**0.5)+1):
        if n%d == 0:
            return False
    return True



number = [9,8,7,6,5,4,3,2,1]

for i in range(8):
    print(number)
    temp_number = copy.deepcopy(number)
    for j in range(Factorial(number[0])):
        if isPrime(Integerise(temp_number)):
            print(Integerise(temp_number))
            break
        temp_number = prevLexicographicPermutation(temp_number)
    number = number[1:]
