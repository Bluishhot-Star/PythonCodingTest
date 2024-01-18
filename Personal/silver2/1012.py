import sys
sys.setrecursionlimit(10 ** 6)

def dfs(adjMatrix, column, row):
    if(adjMatrix[column][row] == -1): return
    adjMatrix[column][row] = 2
    if(adjMatrix[column+1][row] == 1):
        dfs(adjMatrix, column+1, row)
    if(adjMatrix[column][row+1] == 1):
        dfs(adjMatrix, column, row+1)
    if(adjMatrix[column-1][row] == 1):
        dfs(adjMatrix, column-1, row)
    if(adjMatrix[column][row-1] == 1):
        dfs(adjMatrix, column, row-1)



case = int(sys.stdin.readline().rstrip())
for _ in range(case):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    adjMatrix = [[0]*(N+2) for _ in range(M+2)]
    for i in range(M+2):
        adjMatrix[i][0] = -1
        adjMatrix[i][-1] = -1
    for i in range(N+2):
        adjMatrix[0][i] = -1
        adjMatrix[-1][i] = -1
    # print(adjMatrix)
    count = 0

    for i in range(K):
        column, row = map(int, sys.stdin.readline().rstrip().split())
        adjMatrix[column+1][row+1] = 1
    # print(adjMatrix)
    for i in range(1,M+1):
        for j in range(1,N+1):
            if adjMatrix[i][j] == 1:
                dfs(adjMatrix, i, j)
                count+=1
    print(count)