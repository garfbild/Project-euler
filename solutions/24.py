def factorial(n):
    x = 1
    while n>1:
        x = x*n
        n = n-1
    return x
perms = []
nums = [0,1,2,3,4,5,6,7,8,9]
t = 999999
for n in range(9,-1,-1):
    j=0
    while j * factorial(n) <= t:
        j+=1
    t = t-(j-1)*factorial(n)
    perms.append(j-1)

a = []
for p in range(len(perms)):
    a.append(nums[perms[p]])
    del nums[perms[p]]
print(a)
