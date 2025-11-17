import sys
sys.setrecursionlimit(100000)


def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(node1, node2, parent):
    root1 = find(node1, parent)
    root2 = find(node2, parent)

    if root1 == root2:
        return False
    parent[root2] = root1
    return True

def solution(n, costs):
    parent = list(range(n))
    costs.sort(key=lambda x: x[2])
    answer = 0
    for c in costs:
        node1, node2, cost = c
        if union(node1, node2, parent):
            answer += cost
    return answer