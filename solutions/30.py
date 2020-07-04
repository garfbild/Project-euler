#numbers equal to the sum of 5th powers of their decimal digits.
#Since this sum is <= 9^5*d for a d-digit number n >= 10^(d-1),
#there cannot be such a number with more than 6 digits. OEIS
N = 0
for n in range(2,100000):
    strn = str(n)
    s = int(0)
    for d in strn:
        s += int(d)**5
    if s == n:
        print(n)
        N += n
print(N)
