#for d in range(1,phi - 1):
    #if e*d % phi == 1:
        #ds.append(d)
#if ds != []:
    #saved.append([e,ds])

import time

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

p = 1009
q = 3643
n = p*q
print(n)
phi = (p-1)*(q-1)

saved = []
min = 99999
for e in range(1,phi-1):
    if GCD(e,phi) == 1:
        print("e:",e)
        s = 0
        m = 0
        t = time.time()
        while s <= min and m <= n-1:
            c = m**e % n
            if c == m:
                s+=1
            m+=1
        print("time",time.time() - t)
        if s < min:
            min = s
            print("min",min)
        saved.append([e,s])
