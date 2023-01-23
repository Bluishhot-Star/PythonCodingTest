cnt = 0
result = {'index':0, 'value':0}
for i in range(5):
    cnt += 1
    nums = list(map(int, input().split(' ')))
    temp = sum(nums)
    if(result['value'] <= temp):
        result['index'] = cnt
        result['value'] = temp
print(result['index'],result['value'])

