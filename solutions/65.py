List = []
n = 1
while len(List) < 100:
    List.append(1)
    List.append(1)
    List.append(2*n)
    n += 1

List[0] += 1
List = List[0:100]
b = 1
c = List[-1]
for i in range(len(List)-1,0,-1):
    a = List[i-1]
    p = c*a + b
    q = c
    b = q
    c = p
print(b,c)
print(c/b)
listnumerator = list(str(c))
sum = 0
for digit in listnumerator:
    sum += int(digit)
print(sum)
