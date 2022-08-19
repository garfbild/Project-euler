D = 2
d = D**0.5
c = 0
p0,q0 = 1,1
p1,q1 = 3,2
for i in range(1000):
    ptemp = 2*p1+p0
    qtemp = 2*q1+q0
    p0,q0 = p1,q1
    p1,q1 = ptemp,qtemp

    if len(str(p0))>len(str(q0)):
        c+=1
print(c)
