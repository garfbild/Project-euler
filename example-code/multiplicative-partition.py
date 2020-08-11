from sympy import divisors, isprime

#http://oeis.org/A001055

def T(n, m):

    if isprime(n): return 1 if n<=m else 0

    A=filter(lambda d: d<=m, divisors(int(n))[1:-1])

    s=sum(T(n/d, d) for d in A)

    return s + 1 if n<=m else s

def a(n): return T(n, n)

print([a(n) for n in range(1, 106)])
