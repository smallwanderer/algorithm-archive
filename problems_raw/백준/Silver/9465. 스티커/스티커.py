def sol():
  n = int(input())
  temp = [list(map(int, input().split())) for _ in range(2)]
  sticker = temp
  # for a, b in zip(temp[0], temp[1]):
  #   sticker.append([a, b])
  dp = [[0 for _ in range(n)] for _ in range(2)]

  for i in range(n):
    if i == 0:
      dp[0][i], dp[1][i] = sticker[0][i], sticker[1][i]
      continue
    if i == 1:
      dp[0][i], dp[1][i] = sticker[0][i] + dp[1][i-1], sticker[1][i] + dp[0][i-1]
      continue

    dp[0][i] = max(dp[0][i-2], dp[1][i-2], dp[1][i-1]) + sticker[0][i]
    dp[1][i] = max(dp[1][i-2], dp[0][i-2], dp[0][i-1]) + sticker[1][i]

  #find max in 4 block, 2 of necessary:
  if n == 1:
    result = max(dp[0][-1], dp[1][-1])
  else:
    result = max(dp[0][-1], dp[1][-1], dp[0][-2], dp[1][-2])
  # print("result: ", result)
  return result

def testCase():
  T = int(input())

  for _ in range(T):
    print(sol())

testCase()