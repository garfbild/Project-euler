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

p = 19
q = 37
n = p*q
phi = (p-1)*(q-1)

es = []
for e in range(1,phi-1):
    if GCD(e,phi) == 1:
        es.append(e)

m = 19
c = m**e % n
m = c**
