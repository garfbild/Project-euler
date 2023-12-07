from math import comb
def Red(n):
    tally = 0
    for i in range(1,(n//2)+1):
        tally += comb(n-i,i)
    return tally

def Green(n):
    tally = 0
    for i in range(1,(n//3)+1):
        tally += comb(n-2*i,i)
    return tally

def Blue(n):
    tally = 0
    for i in range(1,(n//4)+1):
        tally += comb(n-3*i,i)
    return tally


i = 50
print(i,Red(i))
print(i,Green(i))
print(i,Blue(i))
print(Red(i)+Green(i)+Blue(i))
