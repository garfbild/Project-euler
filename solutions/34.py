def factorial(n):
    x = 1
    while n>1:
        x = x*n
        n = n-1
    return x

saved = []
for i in range(3,100000):
    s = 0
    for digit in str(i):
        s += factorial(int(digit))
    if s == i:
        print(s)
        saved.append(i)

print(saved)
