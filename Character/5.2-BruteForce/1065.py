n = int(input())
count = 0
if n<100:
    print(n)
else:
    count = 99
    for i in range(100,n+1):
        a = ' '.join(str(i)).split(' ')
        intervel = int(a[0]) - int(a[1])
        idx = 1
        while(True):
            temp = int(a[idx]) - int(a[idx+1])
            if(intervel != temp):
                break
            if idx == len(a)-2:
                count+=1
                break
            idx+=1
    print(count)