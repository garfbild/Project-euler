s = 0
x = 1
y = x + 1
z = (x**2 + y**2)**0.5
while x + y + z < 100000000:
    x += 1
    y = x + 1
    c = (x**2 + (x+1)**2)**0.5
    if c == int(c):
        s += 1
print(s)
