for p in range(1001):
    n = 2**p
    t = 0
    for digit in str(n):
        t += int(digit)
    print(p,t)
