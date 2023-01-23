import sys

sys.setrecursionlimit(10**6)

def dfs(Y, X, cnt):
    adjMatrix[Y][X] = 1
    for dY, dX in direc:
        y, x = Y+dY, X+dX
        if (0 <= y < M) and (0 <= x < N) and adjMatrix[y][x] == 0:
            cnt = dfs(y, x, cnt+1)
    return cnt


M, N, K = map(int, sys.stdin.readline().rstrip().split()) #5 7 3
adjMatrix = [[0]*N for _ in range(M)] # 모눈 종이의 점 사이를 한 칸으로
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            adjMatrix[i][j] = 1
direc = [(-1,0), (1,0), (0,-1), (0,1)]
ans = []
for i in range(M): #0~4
    for j in range(N): #0~6
        if adjMatrix[i][j] == 0:
            ans.append(dfs(i,j,1))
print(len(ans))
print(*sorted(ans))