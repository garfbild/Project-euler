def divisors(n):
    divisorlist = []
    for d in range(1,int(n/2 + 2)):
        if n%d == 0:
            divisorlist.append(d)
    return divisorlist

dict  = {}
for i in range(1,10001):
    s = 0
    for num in divisors(i):
        s += num
    dict[i] = s

s=0
for j in range(1,10001):
    n1 = j
    n2 = dict[n1]
    if n2 in dict:
        n3 = dict[n2]
    else:
        n3 = -1
    if n1 == n3 and n1 != n2:
        print(n1,n2,n3)
        s += n1
print(s)
