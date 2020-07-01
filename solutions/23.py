def divisors(n):
    divisorlist = [1]
    for d in range(2,int(n**0.5)+1):
        if n%d == 0 and d!=n:
            divisorlist.append(d)
        if d != n/d:
            divisorlist.append(int(n/d))
    return divisorlist

abundant = []
t = 0
for i in range(1,28124):
    bol = False
    for j in range(len(abundant)):
        if i - abundant[j] in abundant:
            bol = True
            break
    if bol == False:
        t += i
    s = 0
    for divisor in divisors(i):
        s+=divisor
    if s > i:
        abundant.append(i)

print(t)
