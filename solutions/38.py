def check(d):
    strd = str(d)
    n = 1
    r = 2
    while n <= int(len(str(d))/2):
        cm = int(strd[0:n])
        ln = n
        bool = True
        while bool == True and ln < 9:
            bool = False
            for j in range(2):
                print(cm,j,int(strd[ln:ln + n + j]))
                if r*cm == int(strd[ln:ln + n + j]):
                    r += 1
                    ln += n+j
                    bool = True
                    break
        if ln == 9:
            return cm


        n += 1




first = 987654321
test = 192384576
test2 = 918273645
print(check(test2))
