count = 0
for D in range(2,10000):
    d = D**0.5
    if not int(d)**2 == D:
        MNlist = []
        m0 = 0
        n0 = 1
        p = -2
        while str(m0)+str(n0) not in MNlist:
            p += 1
            MNlist.append(str(m0)+str(n0))
            a = int((d+m0)/n0)
            m1 = -(m0-n0*a)
            n1 = (D - (m0-n0*a)**2)/n0
            m0,n0 = m1,n1
        if p%2 == 1:
            count += 1
            print(D)

print(count)
