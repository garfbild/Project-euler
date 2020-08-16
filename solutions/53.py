def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def choose(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

s = 0
for n in range(23,101):
    for r in range(1,n+1):
        if choose(n,r) > 1000000:
            s += 1
print(s)
