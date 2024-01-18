import heapq

li = [9, 4, 2, 8, 5, 1, 7 ,6, 3]
heapq.heapify(li)
print(li)

heapq.heappush(li, 10)
print(li)

sItem = heapq.heappop(li)
print(sItem)
print(li)

heapq.heapreplace(li, 11)
print(li)

largestItems = heapq.nlargest(3, li)
print(largestItems)


smallestItems = heapq.nsmallest(3, li)
print(smallestItems)


# 최대힙
heap = [-num for num in li]  # 모든 원소를 음수로 변환
heapq.heapify(heap)  # 힙으로 변환

print(-heapq.heappop(heap))  # 음수를 다시 양수로 변환하여 출력