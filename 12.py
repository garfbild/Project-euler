def Factors(n):
    factors = 0
    for i in range(1,int(n)):
        if n/i == int(n/i):
            factors+=1
    return factors

trinumber = 1
n = 1
numberFactors = 0
while numberFactors < 500:
    numberFactors = Factors(trinumber)
    print(numberFactors)
    trinumber = trinumber + n
    n+=1
print(trinumber)
