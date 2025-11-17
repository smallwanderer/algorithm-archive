
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def prefix_sum_10986(n, m, arr):
  dp = arr[0]
  dic = {dp % m : 1}
  cnt = 1 if dp % m == 0 else 0
  for i in range(1, n):
    dp += arr[i]
    dic[dp % m] = dic.get(dp % m, 0) + 1
    if dp % m == 0:
      cnt += dic[dp % m]
    else:
      cnt += dic[dp % m]-1 if dic[dp % m] > 1 else 0
  print(cnt)

prefix_sum_10986(n, m, arr)
