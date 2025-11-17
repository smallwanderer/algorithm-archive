# 1517

n = int(input())
arr = list(map(int, input().split()))
tree = [0] * (n+2)

sorted_arr = sorted(set(arr))
rank = {v: i + 1 for i, v in enumerate(sorted_arr)}

def lastBit(bit):
  return bit & (-bit)

def update(idx):
  while idx <= n:
    tree[idx] += 1
    idx += lastBit(idx)

def query(idx):
  fenwick_sum = 0
  while idx > 0:
    fenwick_sum += tree[idx]
    idx -= lastBit(idx)
  return fenwick_sum

result = 0
for i in range(n):
  x = rank[arr[i]]
  result += query(n) - query(x)
  update(x)

print(result)