import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

MOD = 1_000_000_007

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(node*2, start, mid) * init(node*2+1, mid+1, end) % MOD
    return tree[node]

def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        tree[node] = val
        return tree[node]
    mid = (start + end) // 2
    tree[node] = update(node*2, start, mid, idx, val) * update(node*2+1, mid+1, end, idx, val) % MOD
    return tree[node]

def query(node, start, end, left, right):
    if end < left or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    lval = query(node*2, start, mid, left, right)
    rval = query(node*2+1, mid+1, end, left, right)
    return lval * rval % MOD

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [1] * (4 * n)
init(1, 0, n - 1)

for _ in range(m + k):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        update(1, 0, n - 1, a - 1, b)
    else:
        res = query(1, 0, n - 1, a - 1, b - 1)
        print(res)
