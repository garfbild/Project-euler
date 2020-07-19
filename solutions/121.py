def factorial(n):
    x = 1
    while n > 0:
        x = x*n
        n += -1
    return x
print(factorial(5))
