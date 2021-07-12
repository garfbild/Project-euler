max = 0
for a in range(99,90,-1):
    for b in range(99,50,-1):
        s = 0
        n = a**b
        for i in range(len(str(n))):
            s += n//10**(len(str(n))-1-i)%10
        if s > max:
            max = s
print(max)
