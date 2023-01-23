import sys
sys.setrecursionlimit(10**6)

def dfs(x,y, count):
    matrix[x][y] = -1
    for dx, dy in d:
        X, Y = x+dx, y+dy
        if (0 <= X < N) and (0 <= Y < N) and matrix[X][Y] == 1:
            count = dfs(X, Y, count+1)
    return count


N = int(sys.stdin.readline().rstrip())
matrix = []
apt = []
for i in range(N):
    matrix.append([int(i) for i in sys.stdin.readline().rstrip()])

d = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            apt.append(dfs(i,j,1))
print(len(apt))
for i in sorted(apt):
    print(i)

