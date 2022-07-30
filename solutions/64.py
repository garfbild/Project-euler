D = 13
d = D**0.5
for n in range(1,10):
    m0 = 0
    n0 = 1
    contFrac = []
    for i in range(10):
        a = int((d+m0)/n0)
        contFrac.append(a)
        m1 = -(m0-n0*a)
        n1 = (D - (m0-n0*a)**2)/n0
        m0,n0 = m1,n1
print(contFrac)
