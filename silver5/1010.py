def factorial(a):
    if(a == 0): return 1;
    n = a
    sum = 1
    while(n != 1):
        sum *= n
        n -= 1
    return sum;

count = int(input())
for i in range(0, count):
    n, m = map(int, input().split(' '))
    result = factorial(m) / (factorial(m-n)*factorial(n))
    print(int(result))