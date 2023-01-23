def triple(num):
    if '666'in str(num):
        return True
    return False

count = int(input())
num = 666
while(True):
    if(triple(num)):
        count -=1
    if(count == 0):
        break
    num+=1
print(num)