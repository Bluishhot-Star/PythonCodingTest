N = int(input())
M = int(input())
xList = list(map(int,input().split(' ')))
start = 0
end = N
while(True):
    if start == end or end-start == 1:
        print(end)
        break
    iList = []
    height = (start+end)//2
    for i in xList: # 각 M에서 플러스 마이너스
        (x,y) = i-height, i+height
        iList.append((x,y))
    min1,max1 = iList[0]
    min2,max2 = iList[-1]
    if min1 <= 0 and max2 >= N: #조건1: 양 끝단을 비추는가
        dark = 0 # 조건2: 중간에 비추지 않는 부분이 있는지
        for i in range(len(iList)-1):
            min1,max1 = iList[i]
            min2,max2 = iList[i+1]
            if max1 >= min2:
                continue
            else:
                dark = 1
                break
        if dark:
            start = height
        else:
            end = height
    else:
        start = height
            

    
