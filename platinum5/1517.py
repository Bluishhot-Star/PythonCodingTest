import sys
sys.setrecursionlimit(10**6)

def mergeSort(arr):
    global swap_count
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                swap_count += mid - i
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

N = int(sys.stdin.readline().rstrip())
swap_count = 0
numList = list(map(int, sys.stdin.readline().rstrip().split()))
mergeSort(numList)
print(swap_count)