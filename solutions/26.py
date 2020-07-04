import time
def decimal(n):
    if n == 1:
        return[1]
    num = 10
    rs = []
    i = 0
    for i in range(1000):
        while num < n:
            num = num*10
            rs.append(0)
        i=0
        while num - n >= 0:
            i += 1
            num = num - n
        rs.append(i)
        num = num*10
        if num == 0:
            return rs
    return rs

def divisors(n):
    divisorlist = [1]
    for d in range(2,int(n**0.5)+1):
        if n%d == 0 and d!=n:
            divisorlist.append(d)
            if d != n/d:
                divisorlist.append(int(n/d))
    return divisorlist

maxn = 0
maxlen =0
for n in range(1,1001):
    div = divisors(n)[1:]
    bol = True
    for d in range(len(div)):
        if div[d]%2 != 0 and div[d]%5 != 0:
            bol = False
            break
    if div == []:
        bol = False
    if n == 1 or n == 2 or n == 5 :
        bol = True
    if bol == False:
        List = decimal(n)
        l = len(str(n))
        for x in range(len(List)-l):
            Filter = List[x:x+l]
            for y in range(x+1,len(List)-l):
                if List[y:y+l] == Filter:
                    break
            if List[y:y+l] == Filter:
                break
        if y-x > maxlen:
            maxlen = y-x
            maxn = n
print(maxn,maxlen)
