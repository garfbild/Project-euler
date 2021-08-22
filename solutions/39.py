List = [0]*1001
for p in range(4,1001,2):
    for a in range(1,int(p*(1/2))):
        b = (2*p*a-p**2)/(2*a - 2*p)
        if b.is_integer():
            List[p] += 1
            print(p,a,b,a+b+ (a**2+b**2)**0.5)
print(List.index(max(List)))
