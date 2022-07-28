def checkSquare(n):
    if int(n**0.5)**2 == n:
        return True
    return False

def evalCont(c):
    if len(c) == 1:
        return c[0]
    return c[0]+1/(evalCont(c[1:]))

D = 2
sqrtD = D**0.5
contFrac = [0]
a = 1
while a**2 < D:
    a+=1
contFrac[0] = a
for i in range(10):
    j = 1
    contFrac.append(j)
    while evalCont(contFrac)**2 < D:
        j+=1
        contFrac[-1] = j
print(contFrac)



print(evalCont(contFrac))
