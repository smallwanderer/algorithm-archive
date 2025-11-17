n = int(input()) # Number of Integer
nums = sorted(list(map(int, input().split()))) # 5 12 7 10 9 1 2 3 11
# print(*nums) # 1 2 3 5 7 9 10 11 12
key = int(input()) # Number to Find

def two_pointers_3273(key):
  p1, p2 = 0, n-1
  result = 0
  while p1 < p2:
    current_sum = nums[p1] + nums[p2]
    if current_sum == key:
      result += 1
      p1, p2 = p1+1, p2-1 # 서로 다른 양의 정수
    if current_sum < key:
      p1 += 1
    if current_sum > key:
      p2 -= 1
  return result

print(two_pointers_3273(key))