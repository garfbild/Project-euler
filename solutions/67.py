file = open("solutions/triangle.txt","r")
layers = file.read().split('\n')

for i in range(len(layers)):
    layers[i] = layers[i].split(" ")
layers = layers[0:-1]

for i in range(len(layers)-2,-1,-1):
    for j in range(len(layers[i])):
        if int(layers[i+1][j]) > int(layers[i+1][j+1]):
            layers[i][j] = int(layers[i][j])+int(layers[i+1][j])
        else:
            layers[i][j] = int(layers[i][j])+int(layers[i+1][j+1])

print(layers)
