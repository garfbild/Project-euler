# for p in range(3,1001):
#     for a in range(1,int(p**(1/2))):
#         b = (2*p*a-p**2)/(2*a - 2*p)
#         if b.is_integer():
#             print(a,b,a+b+ (a**2+b**2)**0.5)

maxP = 0
maxCount = 0
for p in range(3,1001):
    print(p)
    pCount = 0
    for b in range(1,p//2):
        for a in range(1,b):
            c = p - (a+b)
            if a**2 + b**2 == c**2:
                pCount += 1
    if pCount > maxCount:
        maxP = p
        maxCount = pCount
print(maxP,maxCount)
