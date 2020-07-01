n = ["1","0","0"]
for i in range(99,0,-1):
    t =[]
    for d in n:
        t.append(int(d)*i)
    for p in range(len(t)):
        t[p] = t[p]*10**(len(t)-p-1)
    s=0
    for m in t:
        s+=m
    n = list(str(s))
print(n)
s = 0
for i in n:
    s += int(i)
print(s)
