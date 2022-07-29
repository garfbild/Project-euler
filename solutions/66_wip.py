#https://www.youtube.com/watch?v=3ls3z-UzOSw&ab_channel=BillyWoods-mathematics
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
r = D - a**2



print(evalCont(contFrac))
