# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }

def fibonacci(n):
    a = list()
    if(n==0):
        return [1, 0]
    elif(n==1):
        return [0, 1]
    else:
        a.append(0); a.append(1)
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
        return [a[n-1],a[n]]

cnt = int(input())
for i in range(0, cnt):
    n = int(input())
    result = fibonacci(n)
    print(result[0],result[1])