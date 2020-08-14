eulerCoin = 1504170715041708
n = 1
s = 0
while eulerCoin > 0 and n < 4503599627370517:
    sequence = (1504170715041707*n) % 4503599627370517
    if sequence < eulerCoin:
        s += sequence
        eulerCoin = sequence
        print(eulerCoin)

    n += 1
print(s)
