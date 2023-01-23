dishes = list(input())
stack = 0
temp = ''
for i in dishes:
    if (i != temp):
        temp = i
        stack += 10
    else :
        stack += 5
print(stack)