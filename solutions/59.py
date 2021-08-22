def XOR(a,b):
    XORByte = list("0"*8)
    for i in range(8):
        if a[i] != b[i]:
            XORByte[i] = "1"
    return ''.join(XORByte)

def Bin(a):
    shortbin = bin(int(a))[2:]
    return "0"*(8-len(shortbin))+shortbin

file = open("solutions/cipher.txt","r")
strList = [row.split(",") for row in file.read().split('\n')][0]
binList = []
for i in strList:
    binList = binList+[Bin(int(i))]

#print(strlist)
splitLists = [[],[],[]]
for j in range(len(strList)):
    splitLists[j%3].append(strList[j])
#print(splitLists)

letterCounts = [{},{},{}]
for p in range(3):
    for k in range(len(splitLists[p])):
        try:
            letterCounts[p][splitLists[p][k]] += 1
        except:
            letterCounts[p][splitLists[p][k]] = 1

# print(letterCounts[0])
# print(len(letterCounts[0]))
maxKeyList = [[],[],[]]
maxFreqList = [[],[],[]]
for p in range(3):
    for l in range(6):
        maxFreq = 0
        maxKey = ""
        for m in list(letterCounts[p].keys()):
            if letterCounts[p][m] > maxFreq:
                maxFreq = letterCounts[p][m]
                maxKey = m
        maxKeyList[p].append(maxKey)
        maxFreqList[p].append(maxFreq)
        letterCounts[p][maxKey] = 0
print(maxKeyList)
print(maxFreqList)

#key is three lowercase letters 97-122

candidateKey = []
inputs = [1,1,1]
#just trialed and errored until I got it. making changes that made the text more english like
#turns out most xommon character was SPACE and 2nd popular was e which I hadnt considered until I had found the key
# Freq = e + k => Freq + E = k (XOR ALGEBRA) then k+ cyphertext = plaintext
for p in range(3):
    plain = ord("e")
    cipher = int(maxKeyList[p][inputs[p]])
    candidateKey.append(XOR(Bin(plain),Bin(cipher)))

print(candidateKey)

plaintext = ""
for n in range(len(binList)):
    plaintext = plaintext+chr(int(XOR(candidateKey[n%3],binList[n]),2))
print(plaintext)


s = 0
for t in range(len(plaintext)):
    s += ord(plaintext[t])
print(s)
