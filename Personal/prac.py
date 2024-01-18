# from collections import namedtuple
# Box = namedtuple('Box', ['width','height'])
# b = Box(20,40)
# w,h = b
# print(w, h)


# print(b.width, b.height) # 변수를 이렇게 접근할 수도 있다.
# # >>> 20 40

# print(b)
# # >>> Box(width=20, height=40)

# #(class와 비슷)



# 두 양의 정수가 주어졌을 때, 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램을 작성하시오.
# import sys

# while 1 :
#   n, m = map(int, sys.stdin.readline().rstrip().split())
#   if(n==0 & m==0): break
#   if(n > m): print("Yes")
#   else : print("No")


import sys
T = int(input().rstrip())
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)
                                                                                                                                    