# Disjoint Set
# - Cycle Detection
import sys

def find(x):
  while parent[x] != x:
    parent[x] = parent[parent[x]]
    x = parent[x]
  return x

def cycle_detection(node1, node2):
  node1_root = find(node1)
  node2_root = find(node2)

  if node1_root == node2_root:
    return True
  parent[node2_root] = node1_root
  # if rank[node1_root] < rank[node2_root]:
  #   parent[node1_root] = node2_root
  # elif rank[node1_root] > rank[node2_root]:
  #   parent[node2_root] = node1_root
  # else:
  #   parent[node2_root] = node1_root
  #   rank[node1_root] += 1
  return False

n, m = map(int, sys.stdin.readline().split())
parent = list(range(n))
rank = [0] * n
for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  if cycle_detection(a, b):
    print(i + 1)
    break
else:
    print(0)