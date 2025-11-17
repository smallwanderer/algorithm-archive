import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

class MinimumSegment:
  def __init__(self, n, data):
    self.tree = [0] * (n * 4)
    self.build(1, data, 0, n-1)

  def build(self, node, data, start, end):
    if start == end:
      self.tree[node] = data[start]
    else:
      mid = (start + end) // 2
      self.build(node*2, data, start, mid)
      self.build(node*2+1, data, mid+1, end)
      self.tree[node] = min(self.tree[node*2], self.tree[node*2+1])

  def search(self, node, start, end, left, right):
    if right < start or end < left:
      return float("inf")
    if left <= start and end <= right:
      return self.tree[node]
    mid = (start + end) // 2
    left_search = self.search(node*2, start, mid, left, right)
    right_search = self.search(node*2+1, mid+1, end, left, right)
    return min(left_search, right_search)

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))
segTree = MinimumSegment(n, arr)
for _ in range(m):
  idx1, idx2 = map(int, input().split())
  print(segTree.search(1, 0, n-1, idx1-1, idx2-1))