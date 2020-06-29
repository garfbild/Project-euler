def Factors(n):
    factors = 0
    for i in range(1,int(n/2 + 1)):
        if n/i == int(n/i):
            factors+=1
    return factors

trinumber = 0
n = 0
numberFactors = 0
while numberFactors <500:
    n+=1
    trinumber = trinumber + n
    numberFactors = Factors(trinumber)
print(trinumber)
