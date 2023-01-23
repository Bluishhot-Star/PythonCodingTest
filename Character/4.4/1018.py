'''
#1. 크기가 N*M이고, 흰색과 검은색으로 막 칠해져있는 보드판이 있다.

#2. 이 보드판을 잘라서 8*8크기의 체스판으로 만들려고 한다.

#3. 체스판은 흰색과 검은색이 번갈아가며 체크무늬를 이루어야 한다.

#4. 보드판을 잘라서, 체스판을 만들기 위해서 알맞게 색을 고쳐서 체크무늬를 만들어야 한다.

고쳐야 하는 색의 최소값을 구하라.
'''

n, m = map(int, input().split())
chessMatrix = []
minChessMatrix = []

for x in range(n):
    chessMatrix.append(input())

for X in range(n-7):
    for Y in range(m-7): # 8*8 크기로 자르기 위해서 O O O O O O O O O
        idx1 = 0
        idx2 = 0
        for x in range(X, X+8):
            for y in range(Y, Y+8):
                if (x + y)%2 == 0:
                    if chessMatrix[x][y] != 'W': idx1 += 1
                    if chessMatrix[x][y] != 'B': idx2 += 1
                else :
                    if chessMatrix[x][y] != 'B': idx1 += 1
                    if chessMatrix[x][y] != 'W': idx2 += 1
        minChessMatrix.append(idx1)
        minChessMatrix.append(idx2)

print(min(minChessMatrix))