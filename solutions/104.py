import decimal
from decimal import Decimal

decimal.getcontext().prec = 100
def f (n):
    root5 = Decimal(5**0.5)
    return int((((1+root5)/2)**n - ((1-root5)/2)**n)/root5)

def isPandigital(n):
    if len(n) != 9:
        return False
    count = [0]*10
    for d in str(n):
        if d == "0":
            return False
        elif count[int(d)] == 1:
            return False
        else:
            count[int(d)] = 1
    return True

fn0 = 1
fn1 = 1
modulo = 10**9
k = 2
while True:
    fn2 = (fn1 + fn0) % modulo #we search for all fibonacci numbers where the last 9 are pandigital
    fn0 = fn1
    fn1 = fn2
    k += 1
    if isPandigital(str(fn1)) == True:
        print(k,fn1)
        if isPandigital(str(f(k))[0:9]) == True: # we use the closed form expression of the fibonacci sequence to compute the first 9 digits (not sure how accurate).
            break
print(k,fn1)
