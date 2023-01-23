N, M = map(int, input().split(' '))
numlist = list(map(int, input().split(' ')))
result = 0
for i in range(N-2): #첫 번째부터 뒤에서 세 번째까지
    for j in range(i+1,N-1): #두 번째 부터 뒤에서 두 번째까지
        for k in range(j+1,N): #세 번째 부터 맨 뒤까지
            temp = numlist[i] + numlist[j] + numlist[k] #현재 세션의 값
            if (temp <= M): #M보다 작은 경우
                if(M - result >= M - temp): #현재 항이 M에 가장 가까운 경우
                    result = temp #변경
print(result)