"""
그리디 알고리즘
알고리즘보다는 생각하는 방식
(동전문제...)

c언어에서는 vector를 사용해보자
"""
N = int(input())
A = list(map(int, input().split()))
S = int(input())

i = 0
while(True):
    if(S == 0 or i == N):
        break
    if(S>N):
        Max = A.index(max(A[i:]))
    else:
        if(N-i >= N-(i+S+1)): 
            Max = A.index(max(A[i:i+S+1]))
        else:
            Max = A.index(max(A[i:]))
    if(Max != i):
        temp = A[Max]
        A[Max] = A[Max-1]
        A[Max-1] = temp
        S -= 1
    else:
        i += 1
print(' '.join(str(s) for s in A))