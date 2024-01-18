import sys
sys.setrecursionlimit(10 ** 6)
# 인접행렬 생성
n, m = map(int, sys.stdin.readline().rstrip().split())
adjMatrix = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    adjMatrix[u-1][v-1] = 1;adjMatrix[v-1][u-1] = 1
visited = [False] * n
count = 0

def dfs(n):
    for i in range(len(adjMatrix[n])):
        if adjMatrix[n][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i)

for i in range(n):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)