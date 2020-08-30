def quadraticSolve(a,b,c):
    return (-b + (b**2 - 4*a*c)**0.5)/(2*a)

def NFromblue(B):
    return(1+(8*B**2 - 8*B + 1)**0.5)/2

b = 15
for n in range(7):
    print(8*n**2 % 7, 8*n % 7)

# for b in range(1,1000):
#     if NFromblue(b).is_integer():
#         print(b,b%7)
