#https://www.youtube.com/watch?v=3ls3z-UzOSw&ab_channel=BillyWoods-mathematics
#https://r-knott.surrey.ac.uk/Fibonacci/cfINTRO.html#section6.1
#https://math.stackexchange.com/questions/3341199/cant-find-fundamental-solution-for-x2-61y2-1-through-continued-fraction

def checkSquare(n):
    if int(n**0.5)**2 == n:
        return True
    return False

def evalCont(c):
    if len(c) == 1:
        return c[0]
    return c[0]+1/(evalCont(c[1:]))

def MaxSquare(n):
    return int(n**0.5)

def rContFrac(a):
    n = len(a)
    p0,q0 = a[0],1
    p1,q1 = a[1]*a[0]+1,a[1]
    if n == 1:
        return p0,q0
    elif n == 2:
        return p1,q1
    else:
        for i in range(2,n):
            ptemp = a[i]*p1+p0
            qtemp = a[i]*q1+q0
            p0,q0 = p1,q1
            p1,q1 = ptemp,qtemp

        return p1,q1

D = 61
d = D**0.5

a = MaxSquare(D)
r = (d+a)/(D-a**2)
contFrac = [a]
x,y =0,0
for i in range(100):
    integer = int(r)
    contFrac.append(integer)
    r = 1/(r-integer)
    x,y = rContFrac(contFrac)
    print(contFrac,x,y)
#
# xMax = 0
# DMax = 0
# for D in range(2,1000):
#     if not checkSquare(D):
#         print(D)
#         d = D**0.5
#
#         a = MaxSquare(D)
#         r = (d+a)/(D-a**2)
#         contFrac = [a]
#         x,y =0,0
#         while x**2 - D*y**2 != 1:
#             integer = int(r)
#             contFrac.append(integer)
#             r = 1/(r-integer)
#             x,y = rContFrac(contFrac)
#         print(x,y)
#         if x > xMax:
#             xMax = x
#             DMax = D
#         print()
# print(xMax,DMax)
