def digit(n):
    i = 1
    s = 0
    while n > s+(9*10**(i-1))*i:
        s += (9*10**(i-1))*i
        i += 1
    d = s + (n-s)//i
    return str(d)[(n-s)%i]

def dumb(n):
    i = 0
    d = 1
    string = ""
    while i <= n:
        i += len(str(d))
        string = string + str(d)
        d += 1
    return string[n-1]

# p = 1
# for i in range(1,7):
#     print(int(dumb(10**i)))
#     p = p*int(dumb(10**i))
#     print(10**i)
# print(p)

for n in range(12,1000):
    if dumb(n+1) != digit(n):
        print(n)
