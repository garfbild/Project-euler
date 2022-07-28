import copy
def extEuclid(a,b):
    if a < b:
        temp = a
        a = b
        b = temp
    r0,s0,t0 = a,1,0
    r1,s1,t1 = b,0,1
    while r1 != 0:
        q = int(r0/r1)
        #print(q," ",r0,s0,t0," ",r1,s1,t1)
        temp = [copy.deepcopy(r1),copy.deepcopy(s1),copy.deepcopy(t1)]
        r1 = r0 - q*r1
        s1 = s0 - q*s1
        t1 = t0 - q*t1
        #print(r1,s1,t1)
        r0,s0,t0 = temp[0],temp[1],temp[2]

    return r0,s0,t0,r1,s1,t1

print(extEuclid(3,7))
a,b = -2,-1
for n in range(10):
    print(3*a - 7*b)
    a += 7
    b += 3
    print(a,b)
i = 1
while (-2+(i+1)*7)*7 <1000000:
    i+=1
a = -2+7*i
b = -1+3*i
print(-2+i*7,-1+3*i,3/7,b/a,3/7-b/a,1/(7*a))
