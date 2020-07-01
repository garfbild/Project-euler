def divisors(n):
    divisorlist = [1]
    for d in range(2,int(n**0.5)+1):
        if n%d == 0 and d!=n:
            divisorlist.append(d)
        if d != n/d:
            divisorlist.append(int(n/d))
    return divisorlist

abundant = []
for i in range(1,28124):
    s = 0
    for divisor in divisors(i):
        s+=divisor
    if s > i:
        abundant.append(i)

s = 0
for i in range(1,28124):
    if i % 10 == 0:
        print(i,s)
    for j in range(len(abundant)):
        if i - abundant[j] in abundant:
            print(i,abundant[j])
        else:
            s+=i

print(s)
