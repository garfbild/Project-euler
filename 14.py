dict = {}
def collatz(n):
    count = 1
    while n != 1:
        print(n,count)
        count +=1
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
    return(count)

print(collatz(13))
print(dict)
#max = 0
#for i in range(1000000):
#    n = collatz(i)
#    dict[i] = n
#    if n > max:
#        max = n
