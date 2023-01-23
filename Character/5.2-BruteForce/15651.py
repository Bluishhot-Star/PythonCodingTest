def printList(nList):
    for i in range(len(nList)):
        print(nList[i],end=' ')
    print('\n',end='')

n,m = map(int, input().split(' '))
nList = [1 for i in range(m)]
for i in range(n**m):
    for j in range(m):
        if nList[m-1-j] > n:
            nList[m-1-j] = 1
            nList[m-2-j] += 1
    printList(nList)
    nList[-1] += 1
