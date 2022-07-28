#General binary quadratic equation.
#https://oeis.org/wiki/Binary_Quadratic_Forms_and_OEIS#Dario_Alpern.27s_On-Line_Quadratic_Equation_Solver
#https://www.alpertron.com.ar/QUAD.HTM
#also substitution of u = 2N-1, v = 2B-1 to get negative pells equation v^2 - 2u^2 = -1 which using fundamental solution give the formula from before

B = 15
N = 21

while N < 10**12:
    B, N = 3*B + 2*N - 2, 4*B + 3*N - 3

print(B,N)
