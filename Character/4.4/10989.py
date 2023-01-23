"""
5 2 3 1 4 2 3 5 1 7
(10 이하의 자연수)
배열 10개

숫자세기로 배열 만들기

가장 빠른 정렬 방법

안 쓰는 이유
메모리의 공간을 너무 많이 차지함

readline <- 파이썬에서 할 때 시간을 더 적게 사용함

scanf보다 빨라짐
"""
import sys

cnt = int(input())
numList = [0 for i in range(100001)]

for i in range(cnt):
    a = int(sys.stdin.readline())
    numList[a] += 1
idx = 0
for i in numList:
    if(0 != i):
        for j in range(i):
            print(idx)
    idx += 1
    
