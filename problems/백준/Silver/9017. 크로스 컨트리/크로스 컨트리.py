import collections, sys
input = sys.stdin.readline

def implementation_9017(array):
  count_team = collections.Counter(array)
  score, score_value = collections.defaultdict(list), 1

  for team in array:
    if count_team[team] >= 6:
      score[team].append(score_value)
      score_value += 1

  temp = collections.defaultdict(int)
  for item, val in score.items():
    temp[item] = sum(val[:4])
  temp = sorted(temp.items(), key=lambda x:x[1])

  minimum, min_val = temp[0][0], temp[0][1]
  for i, v in temp:
    if v != min_val:
      return minimum
    minimum = minimum if score[minimum][4] < score[i][4] else i
  return minimum

t = int(input().strip())
for i in range(t):
  n = int(input().strip())
  arr = list(map(int, input().strip().split()))
  print(implementation_9017(arr))