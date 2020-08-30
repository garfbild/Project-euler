import turtle
def insert(n,apparand,string):
    return string[:n]+apparand+string[n+1:]

# D = "Fa"
# for n in range(10):
#     print(n,D)
#     i = 0
#     while i < len(D):
#         if D[i] == "a":
#             D = insert(i,"aRbFR",D)
#             i += 4
#         elif D[i] == "b":
#             D = insert(i,"LFaLb",D)
#             i += 4
#         i += 1

# t = turtle.Turtle()
# t.speed(0)
# t.seth(90)
# t.down()
# for letter in D:
#     if letter == "F":
#         t.forward(10)
#     elif letter == "L":
#         t.left(90)
#     elif letter == "R":
#         t.right(90)
# t.up()

D = "Fa"
for n in range(10):
    print(n,D)
    i = 0
    while i < len(D):
        if D[i] == "a":
            D = insert(i,"aRbFR",D)
            i += 4
        elif D[i] == "b":
            D = insert(i,"LFaLb",D)
            i += 4
        i += 1

saved = []
i = 0
while i < len(D):
    if D[i:i+6] == "FaRbFR":
        i += 6
        saved.append("1")
    elif D[i:i+6] == "FaLbFR":
        i +=5
        saved.append("2")
    else:
        saved.append(D[i])
        i += 1

print(len(saved),saved)



# pos = 0 + 0j #real part is x
# dir = 0 + 1j
# steps = 0
# for i in range(len(D)):
#     if steps == 10**12:
#         break
#     elif D[i] == "F":
#         pos = pos + dir
#         steps += 1
#     elif D[i] == "L":
#         dir = dir*(0 + 1j)
#     elif D[i] == "R":
#         dir = dir*(0 - 1j)
#
# print(steps,pos)
