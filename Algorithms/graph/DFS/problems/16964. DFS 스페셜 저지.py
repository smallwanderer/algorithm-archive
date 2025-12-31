"""
Algoritm: DFS, Backtracking
스페셜저지 : 유저가 출력한 답을 검증하는 코드
문제 링크 : https://www.acmicpc.net/problem/16964
"""

import sys
sys.setrecursionlimit(10**6)

def dfs_16964():
    vertex_count = int(sys.stdin.readline())
    graph = [[] for _ in range(vertex_count + 1)]
    for _ in range(vertex_count - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    answer = list(map(int, sys.stdin.readline().split()))

    traversal_order = []
    def enumerate_dfs_traversal(graph, start=1):
        visited = [False] * (vertex_count + 1)
        traversal = [start]
        stack = [start]
        visited[start] = True

        def bt():
            # print(stack, traversal, visited)
            if len(traversal) == vertex_count:
                traversal_order.append(traversal[:])
                return

            current = stack[-1]
            cand = [n for n in graph[current] if not visited[n]]

            if cand:
                for n in cand:
                    visited[n] = True
                    stack.append(n)
                    traversal.append(n)

                    bt()

                    traversal.pop()
                    stack.pop()
                    visited[n] = False
            else:
                stack.pop()
                bt()
                stack.append(current)

        bt()

    # enumerate_dfs_traversal(graph, start=1)
    # print(1 if answer in traversal_order else 0)

    def special_judge():
        visited = [False] * (vertex_count + 1)
        index = 0
        is_valid = True

        def sj_bt(current):
            nonlocal is_valid, index
            if not is_valid:
                return
            
            print(index, current, answer[index])

            if current != answer[index]:
                is_valid = False
                return
            
            visited[current] = True
            index += 1
            cand = [n for n in graph[current] if not visited[n]]
            if cand:
                if answer[index] not in cand:
                    is_valid = False
                    return
                sj_bt(answer[index])
                
        sj_bt(1)
        print(1 if is_valid else 0)
    
    special_judge()

dfs_16964()