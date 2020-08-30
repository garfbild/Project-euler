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

# while not isBlueValid(B):
#     print(B)
#     B += 1
#unbeleivably slow

print(B,NFromblue(B),NFromblue(B)-10**12)
N = NFromblue(B)
print((B/N)*((B-1)/(N-1)))

#found the minimum value of B to start search from. need to find scalable way to check whether B is valid
#because it seems most values are approximately integer. I don't think this approach is tractable.
#General binary quadratic equation.
#https://oeis.org/wiki/Binary_Quadratic_Forms_and_OEIS#Dario_Alpern.27s_On-Line_Quadratic_Equation_Solver
#https://www.alpertron.com.ar/QUAD.HTM
#I honestly do not understand a single step in the process so will leave as wip even though a solution is found.

B = 15
N = 21

while N < 10**12:
    B, N = 3*B + 2*N - 2, 4*B + 3*N - 3

print(B,N)

# The discriminant is b² − 4⁢a⁢c = 8
#
# Let D be the discriminant. We apply the transformation of Legendre Dx = X + α, Dy = Y + β, and we obtain:
#
# α = 2⁢c⁢d - b⁢e = 4
#
# β = 2⁢a⁢e - b⁢d = 4
#
# 2 X² − Y² = 16 (1)
#
# where the right hand side equals −D (a⁢e² − b⁢e⁢d + c⁢d² + f⁢D)
#
# The algorithm requires that the coefficient of X² and the right hand side are coprime. This does not happen, so we have to find a value of m such that applying one of the unimodular transformations
#
#     X = m⁢U + (m−1)⁢V, Y = U + V
#     X = U + V, Y = (m−1)⁢U + m⁢V
#
# the coefficient of U² and the right hand side are coprime. This coefficient equals 2 m² − 1 in the first case and −(m − 1)² + 2 in the second case.
#
# We will use the first unimodular transformation with m = 1: X = U, Y = U + V (2)
#
# Using (2), the equation (1) converts to:
# U² − 2 U⁢V − V² = 16 (3)
#
# We will have to solve several quadratic modular equations. To do this we have to factor the modulus and find the solution modulo the powers of the prime factors. Then we combine them by using the Chinese Remainder Theorem.
#
# The different moduli are divisors of the right hand side, so we only have to factor it once.
#
# 16 = 24
#
# Searching for solutions U and V coprime.
#
# We have to solve: T² − 2 T − 1 ≡ 0 (mod 16 = 24)
#
# There are no solutions modulo 24, so the modular equation does not have any solution.
#
# Let 2⁢U' = U and 2⁢V' = V. Searching for solutions U' and V' coprime.
#
# From equation (3) we obtain U'² − 2 U'⁢V' − V'² = 16 / 2² = 4
#
# We have to solve: T² − 2 T − 1 ≡ 0 (mod 4 = 22)
#
# There are no solutions modulo 22, so the modular equation does not have any solution.
#
# Let 4⁢U' = U and 4⁢V' = V. Searching for solutions U' and V' coprime.
#
# From equation (3) we obtain U'² − 2 U'⁢V' − V'² = 16 / 4² = 1
#
# We have to solve: T² − 2 T − 1 ≡ 0 (mod 1 = 1)
#
#     T = 0
#
#     The transformation U' = - k (4) converts U'² − 2 U'⁢V' − V'² = 1 to P⁢V'² + Q⁢V'k + R⁢ k² = 1 (5)
#     where: P = (a⁢T² + b⁢T + c) / n = -1, Q = −(2⁢a⁢T + b) = 2, R = a⁢n = 1
#
#     The continued fraction expansion of (Q + D / 4) / R = (1 + 2) / 1 is:
#     2+ // 2// (6)
#
#     Solution of (5) found using the convergent V' / (−k) = 0 / 1 of (6)
#
#     From (4): U' = 1, V' = 0
#
#     U = 4, V = 0
#
#     From (2):
#
#     X = 4, Y = 4
#
#     X + α = 8, Y + β = 8
#
#     Dividing these numbers by D = 8:
#
#     x = 1
#     y = 1
#
#     U = -4, V = 0
#
#     From (2):
#
#     X = -4, Y = -4
#
#     X + α = 0, Y + β = 0
#
#     Dividing these numbers by D = 8:
#
#     x = 0
#     y = 0
#
#     The continued fraction expansion of (−Q + D / 4) / (−R) = (-1 + 2) / (-1) is:
#     -1+ // 1, 1, 2// (7)
#
#     Solution of (5) found using the convergent V' / (−k) = 0 / 1 of (7)
#
#     From (4): U' = 1, V' = 0
#
#     U = 4, V = 0
#
#     From (2):
#
#     X = 4, Y = 4
#
#     X + α = 8, Y + β = 8
#
#     Dividing these numbers by D = 8:
#
#     x = 1
#     y = 1
#
#     U = -4, V = 0
#
#     From (2):
#
#     X = -4, Y = -4
#
#     X + α = 0, Y + β = 0
#
#     Dividing these numbers by D = 8:
#
#     x = 0
#     y = 0
#
#     x = 1
#     y = 1
#
#     x = 0
#     y = 0
#
# Recursive solutions:
#
# xn+1 = 3 ⁢xn + 2 ⁢yn - 2
# yn+1 = 4 ⁢xn + 3 ⁢yn - 3
#
# and also:
# xn+1 = 3 ⁢xn - 2 ⁢yn
# yn+1 = - 4 ⁢xn + 3 ⁢yn + 1
