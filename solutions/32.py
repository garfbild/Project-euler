saved = []
for a in range(10,100):
    for b in range(100,1000):
        s = []
        bol = True
        for digit in str(a)+str(b)+str(a*b):
            if digit not in s and digit != "0" and len(saved) <= 9:
                s.append(digit)
            else:
                bol = False
        if bol == True:
            t = a*b
            if t not in saved:
                saved.append(t)

for a in range(1,10):
    for b in range(1000,10000):
        s = []
        bol = True
        for digit in str(a)+str(b)+str(a*b):
            if digit not in s and digit != "0" and len(saved) <= 9:
                s.append(digit)
            else:
                bol = False
        if bol == True:
            t = a*b
            if t not in saved:
                saved.append(t)
                print(a,b,a*b)

print(sum(saved))
