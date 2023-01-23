count = int(input())
nList = [[0 for col in range(3)]for row in range(count)]
for i in range(count):
    a,b = map(int,input().split())
    nList[i][0] = a
    nList[i][1] = b
for i in range(count):
    for j in range(count):
        if i == j:
            continue
        if nList[i][0] < nList[j][0] and nList[i][1] < nList[j][1]:
            nList[i][2] +=1
    nList[i][2] +=1
for i in range(count):
    print(nList[i][2], end=' ')
print('\n')