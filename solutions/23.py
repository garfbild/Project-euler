def divisors(n):
    divisorlist = []
    for d in range(1,int(n/2)+1):
        if n%d == 0 and d!=n:
            divisorlist.append(d)
    return divisorlist

abundant = []

for i in range(1,28124):
    s = 0
    for divisor in divisors(i):
        s+=divisor
    if s > i:
        abundant.append(i)

print(len(abundant))
print(abundant)
