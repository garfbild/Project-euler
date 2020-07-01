file = open("solutions/names.txt","r")
names = sorted("".join([i for i in file.read() if i != '"']).split(","))
s = 0
for i in range(len(names)):
    t =0
    for l in names[i]:
        t += (ord(l)-64)
    s += (i+1)*t
print(s)
