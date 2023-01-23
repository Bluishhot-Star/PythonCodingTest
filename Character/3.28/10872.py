num = int(input())
if (0 == num or 1 == num):
    print(1)
else:
    result = 1
    for i in range(1, num+1):
        result *= i;
    print(result)
