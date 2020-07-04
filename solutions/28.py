gap = 0
list = [1]
for i in range(2000):
    if i%4 == 0:
        gap += 2
    list.append(list[-1]+gap)
print(list)
print(sum(list))
