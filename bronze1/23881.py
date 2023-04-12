# 선택정렬1
"""
selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2 {
        A[1..last]중 가장 큰 수 A[i]를 찾는다
        if (last != i) then A[last] <-> A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
    }
}
"""


import sys

def selection_sort(N, K, A):
    cnt = 0
    for i in range(N-1, 0, -1): # i : 현재 정렬할 인덱스
        temp = i;
        chg = False
        for j in range(0, i+1): # j : 현재 조사 인덱스
            if A[j] > A[temp]:
                temp = j
                chg = True
        A[i], A[temp] = A[temp], A[i]
        if chg == True : cnt += 1
        if K == cnt : print(A[temp], A[i]);return
    if K > cnt : print(-1);return


N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
selection_sort(N, K, A)