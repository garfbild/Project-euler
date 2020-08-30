def quadraticSolve(a,b,c):
    return (-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a)

def NFromblue(B):
    return(1+(8*B**2 - 8*B + 1)**0.5)/2

def isBlueValid(B):
    D = 8*B**2 - 8*B + 1
    for n in range(1,int(D**0.5)+1):
        if n**2 == D:
            return True
    return False


B = int(quadraticSolve(8,-8,1-(2*10**12 - 1)**2)[0])
print(B)

print(NFromblue(B))
while not isBlueValid(B):
    print(B)
    B += 1

print(B,NFromblue(B),NFromblue(B)-10**12)
N = NFromblue(B)
print((B/N)*((B-1)/(N-1)))

#found the minimum value of B to start search from. need to find scalable way to check whether B is valid
#because it seems must values are approximately integer.
