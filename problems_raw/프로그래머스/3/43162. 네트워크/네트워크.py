def solution(n, computers):
  visit = [0 for _ in range(n)]

  def dfs(i, cnt):
    stack = [i]
    visited = set(stack)

    while stack:
      current_idx = stack.pop(0)

      for node_idx in range(len(computers[current_idx])):
        if computers[current_idx][node_idx] == 0:
          continue
        if node_idx not in visited:
          stack.append(node_idx)
          visited.add(node_idx)

      visit[current_idx] = cnt

  cnt = 1
  for i in range(n):
    if visit[i] != 0:
      continue
    dfs(i, cnt)
    cnt += 1

  return(max(visit))