list = []
for a in range(2,101):
    for b in range(2,101):
        num = a**b
        if num not in list:
            list.append(num)

print(len(list))
