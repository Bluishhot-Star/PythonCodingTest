'''
시간복잡도 박살 버전..ㅎㅎ
'''
# import sys
# from collections import deque

# N,M = map(int, sys.stdin.readline().rstrip().split())
# matrix = []

# for i in range(M):
#     matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
# count = -1
# queue = deque()
# for i in range(M):
#     for j in range(N):
#         if matrix[i][j] == 1:
#             queue.append((i,j))
# temp = []
# d = [(-1,0),(1,0),(0,-1),(0,1)]
# while queue:
#     y, x = queue.popleft()
#     for dy, dx in d:
#         Y, X = y+dy, x+dx
#         if (0 <= Y < M) and (0 <= X < N) and matrix[Y][X] == 0:
#             temp.append((Y, X))
#     if not queue:
#         for i in range(len(temp)):
#             b, a = temp.pop(0)
#             matrix[b][a] = 1
#             queue.append((b,a))
#         count += 1
# for i in range(M):
#     if str(matrix[i]).count('0') != 0:
#         count = -1
#         break
# print(count)


import sys
from collections import deque

N,M = map(int, sys.stdin.readline().rstrip().split())
matrix = []

for i in range(M):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))
queue = deque()
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 1:
            queue.append((i,j))
d = [(-1,0),(1,0),(0,-1),(0,1)]
while queue:
    y, x = queue.popleft()
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and matrix[Y][X] == 0:
            matrix[Y][X] = matrix[y][x] + 1
            queue.append((Y,X))
res = 0            
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            print(-1)
            exit(0)
        res = max(res, matrix[i][j])
print(res-1)