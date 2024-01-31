import sys
N = int(sys.stdin.readline().rstrip())
bookDict = dict()
for i in range(N):
  book = sys.stdin.readline().rstrip()
  if book in bookDict:
    bookDict[book] += 1
  else:
    bookDict[book] = 1

result = sorted([key for key, value in bookDict.items() if value == max(bookDict.values())])
print(result[0])
