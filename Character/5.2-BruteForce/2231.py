def func(n):
    n = list(n)
    result = 0
    temp = ''
    for i in n:
        result += int(i)
    for i in n:
        temp += i
    result += int(temp)
    return result

n = input()
num = ''
for i in n:
        num += i
for i in range(int(n)):
    if  int(num) == func(str(i)):
        answer = i
        break
    answer = 0
print(answer)