# for n in range(1,100):
#     print(n,int(n*(n+1)/2),int(n*(n+1)/2)%n)

# for k in range(1,100):
#     print(k,int(k*(3*k-1)/2),int(k*(3*k-1)/2)%k)

# for r in range(1,100):
#     print(r,int(r*(2*r-1)),int(r*(2*r-1))%r)
def polynomial(a,b,c):
    return (-b+((b**2) - (4*a*c))**0.5)/(2*a)
for r in range(143,1000000):
    hex = r*(2*r-1)
    x = polynomial(3,-1,-2*hex)
    if x.is_integer():
        print(hex,x)
