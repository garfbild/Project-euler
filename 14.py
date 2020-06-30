dict = {}
def collatz(n):
    count = 1
    while n != 1:
        if n%2 == 0:
            n = n/2
            if str(n) in dict:
                count += dict[str(n)]
                break
        else:
            n = 3*n+1
            if str(n) in dict:
                count += dict[str(n)]
                break
        count +=1
    return(count)

max = 0
for i in range(1,1000000):
    n = collatz(i)
    dict[i] = n
    if n > max:
        max = n
        print(i,max)
print(dict["13"])
