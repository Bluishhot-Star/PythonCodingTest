import sys
sys.setrecursionlimit(10**6)

def removeTreeDfs(A, removeIndex):
    A[removeIndex] = None
    for i in range(len(A)):
        if removeIndex == A[i]:
            removeTreeDfs(A, i)



N = int(sys.stdin.readline().rstrip()) # 노드개수
nodeList = list(map(int,sys.stdin.readline().rstrip().split())) # 노드 리스트
trueList = [True for i in range(N)]
removeIndex = int(sys.stdin.readline().rstrip()) # 삭제 인덱스

# remove subTree
removeTreeDfs(nodeList, removeIndex)

# find leaf node
leafCnt = 0
for i in range(N):
    if nodeList[i] != None and i not in nodeList:
        leafCnt += 1

print(leafCnt)