count = int(input())
tList = []
for i in range(count):
    tList.append(int(input()))
for i in tList:
    start = 1
    end = i
    while(1):
        mid = (start + end) // 2
        if(start == end or end-start == 1):
            print(end)
            break
        result = 0
        temp = mid
        while(1):
            result += temp
            if(result > i):
                start = mid+1
                break
            elif(result == i):
                end = mid-1
                break
            else:
                temp = temp+1