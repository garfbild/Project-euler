from math import comb
def Red(n):
    for i in range(1,(n//2)+1):
        comb(n-i,i)
        print(n-i,i,comb(n-i,i))

Red(4)
Red(6)
Red(7)
