import math
def solution():
    n = int(input())
    a = list(map(int, input().split(" ")))
    b, c = input().split(" ")
    result = 0

    for i in range(n):
        if a[i]-int(b) < 0:
            result += 1
            continue
        result += 1 + math.ceil((a[i]-int(b))/int(c))

    return result


print(solution())