import sys
sys.setrecursionlimit(1000000)

n = sys.stdin.readline().strip()
dp = [-1] * (len(n) + 1)

def isValid(num):
  return 1 <= num <= 26

def dfs(idx):
  if idx == len(n): return 1  # 해석 성공

  if dp[idx] != -1: return dp[idx]

  if n[idx] == '0': return 0

  result = dfs(idx + 1)

  if idx + 1 < len(n):
    num = int(n[idx:idx+2])
    if isValid(num):
      result += dfs(idx+2)

  dp[idx] = result % 1000000
  return dp[idx]

print(dfs(0) if n != "0" else 0)