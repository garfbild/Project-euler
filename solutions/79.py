file = open("solutions/keylog.txt","r")
List = file.read().split('\n')
List = List[:-1]
print(List)
delList = []
delNames = []
for i in range(len(List)):
    if List[i] in List[:i] + List[i+1:] and List[i] not in delNames:
        delList.append(i)
        delNames.append(List[i])
List = [List[i] for i, j in enumerate(List) if i not in delList]
print(List)
start = List[0]
for j in range(len(List)-1):
    
