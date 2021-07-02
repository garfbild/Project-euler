def efficentPower(a,n):
    temp = a
    for i in range(n-1):
        temp = (temp*a)%10000000000
        #print(str(a**(i+2))[-10:],temp)
    return temp

print(str(999**999)[-10:])
print(efficentPower(999,999))
s = 0
for i in range(1000,0,-1):
     s += efficentPower(i,i)
print(s,str(s)[-10:])
