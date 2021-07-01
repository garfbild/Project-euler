def isPentagonal(p):
    x = (1+(1 + 24*p)**0.5)/6
    if x.is_integer():
        return True
    return False

def Pent(n):
    return n*(3*n-1)/2

for x in  range(1,1000000):
    for y in range(x-1,0,-1):
        if isPentagonal(Pent(x)+Pent(y)) and isPentagonal(Pent(x)-Pent(y)):
            print(abs(Pent(x)-Pent(y)))
