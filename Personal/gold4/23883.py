import sys

def selection_sort(N, K, A):
    # 정렬된 리스트
    sortedA = sorted(A)
    numDict = {}
    
    # 딕셔너리  key : A원소 value : 정렬전 인덱스
    for i, j in enumerate(A):
      numDict[j] = i
      
    cnt = 0
    for i in range(N-1, -1, -1): # i : 현재 정렬할 인덱스
        if sortedA[i] != A[i]: # 현재 인덱스가 아니면?
          result = [A[i], sortedA[i]]
          A[i], A[numDict[sortedA[i]]] = A[numDict[sortedA[i]]], A[i]
          numDict[result[0]], numDict[result[1]] = numDict[result[1]], numDict[result[0]]
          cnt += 1
        if K == cnt : print(*result);return
    if K > cnt : print(-1);return


N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
selection_sort(N, K, A)


