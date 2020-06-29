def tN(n):
    return int(n*(n+1)/2)

def Factors(n):
    f = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            f+=1
    return f*2

j = 0
numFactors = 0
while numFactors < 500:
    j+=1
    t = tN(j)
    numFactors = Factors(t)
    if numFactors%100 == 0:
        print(j,numFactors)
print(j)
