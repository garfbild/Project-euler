
p = [1,1]
n = 2
bol = False
while bol == False:
    j = 0
    Q = []
    # Q is list of Eulers pentagonal numbers < n
    while j*(3*j - 1)/2 <= n:
        if j > 0:
            j = j*-1
        else:
            j = (j*-1) + 1
        Q.append(int(j*(3*j - 1)/2))
    Q = Q[:-1]
    p.append(0)
    counter = 0
    #compute the recursive formula for the partition function
    for j in range(len(Q)):
        if counter == 0 or counter == 1:
            p[-1] += p[-1-Q[j]]
        else:
            p[-1] += p[-1-Q[j]]*-1
        counter += 1
        if counter == 4:
            counter = 0

    if p[-1] % 1000000 == 0:
        print(n)
        bol = True
    else:
        n+=1
