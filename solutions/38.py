def check(d):
    for n in range(1,4):
        cm = d//10**(9-n)
        for j in range(3):
            r = 2
            ln = n
            while r*cm == d//10**(9-(r*n)-j)%10**(n+j) and ln < 9:
                print(d//10**(9-(r*n)-j)%10**(n+j))
                ln += n+j
                r += 1

            if ln == 9:
                return cm,[i for i in range(1,r)]



first = 987654321
test = 192384576
test2 = 918273645
print(check(test2))
