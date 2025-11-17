def solution(n, results):
    from collections import defaultdict

    win = defaultdict(list)
    lose = defaultdict(list)

    for a, b in results:
        win[a].append(b)     # a가 이긴 선수들
        lose[b].append(a)     # b가 진 선수들

    def dfs(start, graph):
        visited = set()
        stack = [start]
        while stack:
            cur = stack.pop()
            for next_node in graph[cur]:
                if next_node not in visited:
                    visited.add(next_node)
                    stack.append(next_node)
        return visited

    answer = 0
    for i in range(1, n + 1):
        win_set = dfs(i, win)
        lose_set = dfs(i, lose)

        if len(win_set) + len(lose_set) == n - 1:
            answer += 1

    return answer