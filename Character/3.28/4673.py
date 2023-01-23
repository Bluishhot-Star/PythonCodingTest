temp = 1
nonResultList = list()
while(temp < 10000):
    nonResult = 0
    itemp = ' '.join(str(temp)).split(' ') #숫자를 하나씩
    for i in itemp:
        nonResult += int(i) #자릿수 마다 숫자 다 더하기
    nonResult += temp #마지막으로 수 자체를 더하기
    nonResultList.append(nonResult) #더한 값을 값이 아닌 리스트에 더해준다.
    if (temp not in nonResultList): #값이 아닌 리스트에 현재 반복의 temp가 없으면
        print(temp) #프린트
    temp += 1 #다음 반복을 위해 +1
    
