#https://en.wikipedia.org/wiki/Permutation#Algorithms_to_generate_permutations

def check(d):
    strd = str(d)
    n = 1
    r = 2
    while n <= int(len(str(d))/2):
        cm = int(strd[0:n])
        ln = n
        bool = True
        while bool == True and ln < 9:
            bool = False
            for j in range(3):
                if r*cm == int(strd[ln:ln + n + j]):
                    r += 1
                    ln += n+j
                    bool = True
                    break
        if ln == 9:
            return True
        n += 1
    return False

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def nextLexicographicPermutation(a):
    n = len(a)
    k_copy = -1
    for k in range(n-2,-1,-1):
        if a[k] < a[k+1]:
            k_copy = int(k)
            break
    if k_copy == -1:
        return a
    for l in range(n-1,k_copy-1,-1):
        if a[k_copy] < a[l]:
            l_copy = int(l)
            break
    temp = a[k_copy]
    a[k_copy] = a[l_copy]
    a[l_copy] = temp

    return a[:k_copy+1] + a[k_copy+1:][::-1]

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

def Integerise(a):
    i = 0
    n = len(a)
    for x in range(n):
        i += a[x]*10**(n-x-1)
    return i

test = 192384576
test2 = 918273645

number = [9,8,7,6,5,4,3,2,1]

bool = True

while bool:
    number = prevLexicographicPermutation(number)
    if check(Integerise(number)):
        bool = False
print(number)
