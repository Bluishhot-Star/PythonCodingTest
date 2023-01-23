hour = list(range(0,24))
min = list(range(0,60))
cHour, cMin=tuple(map(int, input().split(' ')))

mIdx = cMin - 45
if(mIdx < 0):
    aHour = hour[cHour - 1]
else:
    aHour = cHour
aMin = min[cMin - 45]
print(aHour, aMin)