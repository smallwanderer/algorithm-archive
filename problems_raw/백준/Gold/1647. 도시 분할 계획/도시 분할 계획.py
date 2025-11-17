# 1657 : MST
#   - Kruskal

import sys

# Number of House n, Number of Road m
n, m = map(int, sys.stdin.readline().split())
edges = []

for _ in range(m):
  h1, h2, w = map(int, sys.stdin.readline().split())
  edges.append((h1, h2, w))

def separation_plan_kruskal(edges):
  parent = list(range(n+1))

  def _find(node):
    root = node
    while parent[root] != root:
      root = parent[root]

    while parent[node] != root:
      next_node = parent[node]
      parent[node] = root
      node = next_node

    return root

  def _union(node1, node2):
    root1 = _find(node1)
    root2 = _find(node2)

    if root1 == root2:
      return False
    parent[root2] = root1
    return True

  max_link = 0
  sorted_edges = list(sorted(edges, key=lambda x: x[2]))

  sum_of_road = 0
  for edge_data in sorted_edges:
    node1, node2, weight = edge_data

    if _union(node1, node2):
      sum_of_road += weight
      max_link = max(weight, max_link)

  return sum_of_road - max_link

print(separation_plan_kruskal(edges))