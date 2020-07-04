coins = [200,100,50,20,10,5,2,1]
target = 200
def findSolutions(n,coins,s):
    if n == 0:
        return s + 1
    for c in range(len(coins)):
        if n - coins[c] >= 0:
            s = findSolutions(n-coins[c],coins[c:],s)
    return s

print(findSolutions(200,coins,0))
