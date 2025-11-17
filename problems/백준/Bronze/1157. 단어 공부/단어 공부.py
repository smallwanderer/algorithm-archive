import collections

n = collections.Counter(input().upper()).most_common(2)
print(n[0][0] if len(n) == 1 else "?" if n[0][1] == n[1][1] else n[0][0])
