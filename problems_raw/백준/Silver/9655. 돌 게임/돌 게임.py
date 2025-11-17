import sys

n = int(sys.stdin.readline().strip())

def sol(n):
    return "SK" if n % 2 == 1 else "CY"

print(sol(n))
