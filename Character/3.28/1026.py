# cnt = int(input())
# Alist = list(map(int,input().split(' ')))
# Blist = list(map(int,input().split(' ')))
# templist = [0 for i in range(cnt)]
# Alist.sort()
# sortedBlist=sorted(Blist)
# sortedBlist.reverse()
# for i in range(cnt):
#     tempIndex = Blist.index(sortedBlist[i])
#     templist[tempIndex] = Alist[i]
# print(templist)
# result = 0
# for j in range(cnt):
#     result += templist[j]*Blist[j]
# print(result)

cnt = int(input())
Alist = list(map(int,input().split(' ')))
Blist = list(map(int,input().split(' ')))

Alist.sort()
Alist.reverse() #내림차순

Btemplist = Blist #B값 담기

result = 0
for a in Alist:
    templist = [a*b for b in Btemplist] #A리스트 B리스트 곱하기
    sorted_templist = sorted(templist)  #곱한 리스트를 오름차순
    result += sorted_templist[0] # 오름차순한 리스트의 0번째를 값에 더함(최소값)
    Btemplist.pop(templist.index(sorted_templist[0])) #최소값에 해당하는 값 더하고 빼기

print(result)
