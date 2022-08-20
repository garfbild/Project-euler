def bouncyCheck(n):
    p = len(str(n))
    inc = True
    dec = True
    i = 0
    while i < p-1 and (inc == True or dec == True):
        if n//(10**(p-i-1))%10 < n//(10**(p-i-2))%10:
            dec = False
        elif n//(10**(p-i-1))%10 > n//(10**(p-i-2))%10:
            inc = False
        i+=1
    if inc == False and dec == False:
        return True
    else:
        return False
c = 0
n = 100
while 100*c/99 != n:
    n+=1
    if bouncyCheck(n):
        c += 1

print(c,n)
