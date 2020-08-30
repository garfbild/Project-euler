def quadraticSolve(a,b,c):
    return (-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(quadraticSolve(1,2,1))
