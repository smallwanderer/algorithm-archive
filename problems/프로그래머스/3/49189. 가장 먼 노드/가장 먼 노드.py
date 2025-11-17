def solution(n, edge):
    nodes = dict([(x, []) for x in range(1, n+1)])
    for e in edge:
        nodes[e[0]].append(e[1])
        nodes[e[1]].append(e[0])
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    
    stack = [1]
    while stack:
        current = stack.pop(0)
        for node in nodes[current]:
            if dp[node] != 0:
                continue
            dp[node] = dp[current] + 1
            stack.append(node)
    return dp.count(max(dp))            
