case = int(input())
for i in range(case):
    volume, targetIdx = tuple(map(int, input().split(' ')))
    starList = list(map(int, input().split(' ')))
    if(volume == 1):
        print(1)
        continue;

    cnt = 0;

    while(True):
        if(starList[0] == max(starList)): #0번째가 중요도 우위
            cnt += 1 #빠져나간 cnt +1
            if(targetIdx == 0): #0번째가 target일 경우
                print(cnt) #cnt 출력
                break;
            volume -= 1 #문서 개수 -1
            targetIdx -= 1 #targetIdx의 순서 앞당기기
            starList.pop(0)
            continue #다음 반복
        else: #0번째가 중요도 우위X
            temp = starList.pop(0) 
            starList.append(temp)
            if(targetIdx == 0): #0번째가 target이었을 경우
                targetIdx = volume-1 #targetIdx 맨 뒤로
            else:
                targetIdx -= 1 #targetIdx 앞당기기
            