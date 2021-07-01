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

    return r0,s0,t0

d = 12000
t = 0
for d in range(4,d+1):
    print(d)
    for n in range(max(int(d/3)+1,1),int(d/2)+1):
        if extEuclid(n,d)[0] == 1:
            t += 1
print(t)
