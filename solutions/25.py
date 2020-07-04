import time
fib = [1,1]
n = 2
fibn = 2
while len(str(fibn)) < 1000:
    fibn = fib[0]+fib[1]
    fib[1] = fib[0]
    fib[0] = fibn
    n+=1
print(n)
