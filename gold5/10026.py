import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, target):
    visited[x][y] = 1
    for dx, dy in d:
        X, Y = x+dx, y+dy
        if (0<= X < N) and (0<= Y < N) and matrix[X][Y] == target and visited[X][Y] == 0:
            dfs(X,Y, target)

def dfsRG(x, y, target):
    if target == 'R' or target == 'G' : target = 'A'
    visited[x][y] = 1
    for dx, dy in d:
        X, Y = x+dx, y+dy
        if (0<= X < N) and (0<= Y < N) and visited[X][Y] == 0:
            if matrix[X][Y] == 'R' or matrix[X][Y] == 'G': matrix[X][Y] = 'A'
            if matrix[X][Y] == target:
                dfsRG(X,Y, target)

N = int(sys.stdin.readline().rstrip())
matrix = []
normal = 0; redGreen = 0

visited = [[0]*N for i in range(N)]
for i in range(N):
    line = sys.stdin.readline().rstrip()
    matrix.append([i for i in line])

d = [(-1,0),(1,0),(0,-1),(0,1)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j, matrix[i][j])
            normal+=1
print(normal, end=' ')

visited = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfsRG(i, j, matrix[i][j])
            redGreen+=1
print(redGreen)