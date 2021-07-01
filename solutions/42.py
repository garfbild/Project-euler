file = open("solutions/words.txt","r")
words = file.read().split('\n')
splitwords = [words[i].split(',') for i in range(len(words))]
justwords = [splitwords[i] for i in range(len(splitwords))][0]
juststrwords = [str(word)[1:-1] for word in justwords]
print(juststrwords)
def wordtonumber(word):
    total = 0
    for letter in word:
        total += ord(letter)-64
    return int(total)

max = 0
for i in range(len(juststrwords)):
    if wordtonumber(juststrwords[i]) > max:
        max = wordtonumber(juststrwords[i])

print(max)

def triangleNumber(n):
    return (n*(n+1))/2

n = 0
triangleNumbers = []
while triangleNumber(n) < max:
    n += 1
    triangleNumbers.append(int(triangleNumber(n)))

print(n,triangleNumbers)

count = 0
for i in range(len(juststrwords)):
    if wordtonumber(juststrwords[i]) in triangleNumbers:
        count += 1
        print(juststrwords[i],wordtonumber(juststrwords[i]))
print(count)
