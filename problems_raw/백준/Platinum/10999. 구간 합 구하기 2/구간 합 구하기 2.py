# 백준 10999

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n, m, k = map(int, input().split())
size = 1 << (n-1).bit_length()

tree = [0] * (2 * size)
lazy = [0] * (2 * size)

data = [int(input()) for _ in range(n)]
# for i in range(n):
#   tree[size + i] = data[i]
# for i in range(size - 1, 0, -1):
#   tree[i] = tree[i * 2] + tree[i * 2 + 1]

def build(node, l, r):
  if l == r:
    tree[node] = data[l]
  else:
    mid = (l + r) // 2
    build(node*2, l, mid)
    build(node*2+1, mid+1, r)
    tree[node] = tree[node*2] + tree[node*2+1]

def propagate(node, l, r):
  if lazy[node] != 0:
    tree[node] += (r - l + 1) * lazy[node]
    if l != r:
      lazy[node * 2] += lazy[node]
      lazy[node * 2 + 1] += lazy[node]
    lazy[node] = 0

def update(node, l, r, start, end, val):
  propagate(node, l, r)
  if end < l or r < start:
    return
  if start <= l and r <= end:
    lazy[node] += val
    propagate(node, l, r)
    return
  mid = (l + r) // 2
  update(node * 2, l, mid, start, end, val)
  update(node * 2 + 1, mid + 1, r, start, end, val)
  tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, l, r, start, end):
  propagate(node, l, r)
  if end < l or r < start:
    return 0
  if start <= l and r <= end:
    return tree[node]
  mid = (l + r) // 2
  return query(node * 2, l, mid, start, end) + query(node * 2 + 1, mid + 1, r, start, end)

build(1, 0, n-1)
for _ in range(m+k):
  op = list(map(int, input().split()))
  if op[0] == 1:
    update(1, 0, n - 1, op[1] - 1, op[2] - 1, op[3])
  else:
    print(query(1, 0, n - 1, op[1] - 1, op[2] - 1))
