def XOR(key,byte):
    XORByte = list("0"*8)
    for i in range(8):
        if key[i] != byte[i]:
            XORByte[i] = "1"
    return ''.join(XORByte)

file = open("solutions/cipher.txt","r")
strlist = [row.split(",") for row in file.read().split('\n')][0]
binlist = []
for i in strlist:
    shortbin = bin(int(i))[2:]
    uniformbin = "0"*(8-len(shortbin))+shortbin
    binlist = binlist+[uniformbin]

for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            plaintext = []
            key = ["0"*(8-len(bin(a)[2:]))+bin(a)[2:],"0"*(8-len(bin(b)[2:]))+bin(b)[2:],"0"*(8-len(bin(c)[2:]))+bin(c)[2:]]
            for j in range(len(binlist)):
                plaintext = plaintext+[chr(int(XOR(key[j%3],binlist[j]),2))]
            print(plaintext)
