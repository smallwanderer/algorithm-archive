import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = 0
for i in range(n):
    if arr[i] == 0:
        continue

    if i < n - 2 and arr[i + 1] > arr[i + 2]: # consider 1 4 2
        buy = min(arr[i], arr[i + 1] - arr[i + 2])
        arr[i] -= buy
        arr[i + 1] -= buy
        result += buy * 5

    if i < n - 2: # consider 1 2 3
        buy = min(arr[i], arr[i + 1], arr[i + 2])
        arr[i] -= buy
        arr[i + 1] -= buy
        arr[i + 2] -= buy
        result += buy * 7

    if i < n - 1: # consider 1 2
        buy = min(arr[i], arr[i + 1])
        arr[i] -= buy
        arr[i + 1] -= buy
        result += buy * 5

    result += arr[i] * 3
    arr[i] = 0
print(result)
