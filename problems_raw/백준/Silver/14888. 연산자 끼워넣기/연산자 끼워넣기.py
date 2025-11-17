import copy

n = int(input())
a = list(map(int, input().split(' ')))
operator = list(map(int, input().split(' ')))

a_idx = 0
op = [0, 0, 0, 0]
result = []

def operation(a, b, index):
    if index == 3:
        if a < 0:
            return -(-a // b)
        return a // b
    switch = {0: lambda x,y: x+y, 1: lambda x,y: x-y, 2: lambda x,y: x*y}
    return switch[index](a,b)

def bt(a0, a_idx, op):
    if a_idx == n-1:
        result.append(a0)
        return

    for op_idx in range(len(op)):
        if operator[op_idx] <= op[op_idx]:
            continue
        bt_op = copy.deepcopy(op)
        bt_op[op_idx] += 1
        a1 = operation(a0, a[a_idx+1], op_idx)
        bt(a1, a_idx+1, bt_op)

bt(a[0], a_idx, op)
print(max(result))
print(min(result))