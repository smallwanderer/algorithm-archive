import math
import heapq

n = int(input())
expire = list(map(int, input().split()))
plan = list(map(int, input().split()))
plan_heap = []
expire_heap = []
ADD_EXPIRE = 30

cnt = 0
for i in range(n):
  temp = math.ceil((max(0, plan[i]-expire[i])) / ADD_EXPIRE)
  heapq.heappush(plan_heap, (plan[i], i))
  heapq.heappush(expire_heap, (temp * ADD_EXPIRE + expire[i], plan[i]))
  cnt += temp

while plan_heap:
  current_plan = heapq.heappop(plan_heap)
  while True:
    minimum_expire = heapq.heappop(expire_heap)
    if current_plan[0 ] == minimum_expire[1]:
      break
    heapq.heappush(expire_heap, (minimum_expire[0]+ADD_EXPIRE, minimum_expire[1]))
    cnt += 1

print(cnt)




