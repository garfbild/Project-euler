coins = [200,100,50,20,5,2,1]
target = 200
def findSolutions(n,coins,s):
    if n == 0:
        return s + 1
    for coin in coins:
        if n - coin >= 0:
            print(coin)
            s += findSolutions(n-coin,coins,s)
    return s

print(findSolutions(10,coins,0))
