def factorial(n):
    x = 1
    while n>1:
        x = x*n 
        n = n-1
    return x


def combinations(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print(combinations(40,20))
