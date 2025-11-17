import sys

def solution():
  n = int(sys.stdin.readline())
  boxes = list(map(int, sys.stdin.readline().split()))
  box_dp = [1] * n

  for box_idx in range(n):
    for dp_idx in range(box_idx+1, n):
      if boxes[dp_idx] > boxes[box_idx]:
        box_dp[dp_idx] = max(box_dp[dp_idx], box_dp[box_idx]+1)
  print(max(box_dp))

solution()