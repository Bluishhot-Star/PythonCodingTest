# import math
# def func(start, end):
#     for i in range(start, end+1):
#         tF = True
#         for j in range(2, int(math.sqrt(i)+1)):
#             if(i % j == 0): 
#                 tF = False
#         if tF == True: print(i)
# start, end = map(int,input().split(' '))
# func(start, end)

import math
import time
def primeNumber(min, max):
    numList = [True for i in range(max + 1)] 
    numList[1] = False
    for i in range(2, int(math.sqrt(max)) + 1):
        if numList[i] == True:
            j = 2
            while i * j <= max:
                numList[i * j] = False
                j += 1
    for i in range(min, max + 1):
        if numList[i]:
            print(i)

start, end = map(int,input().split(' '))
primeNumber(start, end)