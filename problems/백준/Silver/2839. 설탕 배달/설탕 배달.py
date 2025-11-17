n = int(input())

def sugar_delivery2(n):
    for i in range(n//5, -1, -1):
        leftover = n-(i*5)
        if leftover % 3 == 0:
            return leftover//3 + i
    return -1

print(sugar_delivery2(n))