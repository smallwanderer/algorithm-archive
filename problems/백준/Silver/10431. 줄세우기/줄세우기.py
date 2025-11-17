import sys

n = int(sys.stdin.readline())

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    test_case = data[0]
    students = data[1:]
    cnt = 0
    for i in range(1, len(students)):
        current = students[i]
        j = i - 1
        while j >= 0 and students[j] > current:
            students[j + 1] = students[j]
            cnt += 1
            j -= 1
        students[j + 1] = current
    print(test_case, cnt)
