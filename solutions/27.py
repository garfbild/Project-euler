def divisors(n):
    divisorlist = [1]
    if n < 0:
        n = -n
    for d in range(2,int(n**0.5)+1):
        if n%d == 0 and d!=n:
            divisorlist.append(d)
            if d != n/d:
                divisorlist.append(int(n/d))
    return divisorlist

def polynomial(a,b,n):
    return n**2 + a*n + b

blist = []
for b in range(1,1001):
    if divisors(b) == [1]:
        blist.append(b)

alist = []
for a in range(1,1001):
    alist.append(a)
    alist.append(-a)

maxn = 0
maxc = []
for a in alist:
    for b in blist:
        n = 0
        while divisors(polynomial(a,b,n)) == [1]:
            n += 1
        if n > maxn:
            maxn = n
            maxc = [a,b]
print(maxn,maxc)
