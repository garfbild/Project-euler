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

def Factorial(n):
    if n == 1:
        return n
    else:
        return n*Factorial(n-1)

def INT(x):
    return int("".join(str(i) for i in x))

number = [9,8,7,6,5,4,3,2,1,0]
primes = [2,3,5,7,11,13,17]

D4 = [0,2,4,6,8]
D6 = [5]
D7 = [0]

s = 0

print(INT([0,8,7,6,5,4,3,2,1,9]))

for i in range(Factorial(len(number))):
    if number[3] in D4:
        bool = True
        i = 0
        while bool == True and i < len(primes):
            if INT(number[1+i:4+i])%primes[i] != 0:
                bool = False
            i+=1

        if bool == True:
            print(INT(number))
            s+=INT(number)
    number = prevLexicographicPermutation(number)
print(s)
