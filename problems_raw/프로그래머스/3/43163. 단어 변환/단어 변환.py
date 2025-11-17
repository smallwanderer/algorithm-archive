import collections
def solution(begin, target, words):
  words.append(begin)
  relationship = _make_relationship(words)
  queue = collections.deque([begin])
  dp = dict.fromkeys(words, 0)
  while queue:
    current = queue.popleft()
    if current == target:
      return dp[current]
    for ad_node in relationship[current]:
      if dp[ad_node] == 0:
        dp[ad_node] = dp[current] + 1
        queue.append(ad_node)
  return 0

def _compare(word1, word2):
  return sum(a!=b for a, b in zip(word1, word2)) == 1

def _make_relationship(words):
  result = collections.defaultdict(list)
  for word in words:
    result[word] = [word2 for word2 in words if _compare(word, word2)]
  return result