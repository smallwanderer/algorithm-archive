import heapq, sys

n = int(sys.stdin.readline().strip())
min_heap = []
max_heap = []
answer = []

for i in range(n):
  number = int(sys.stdin.readline().strip())

  heapq.heappush(max_heap, -number)

  if min_heap and -max_heap[0] > min_heap[0]:
    heapq.heappush(min_heap, -heapq.heappop(max_heap))
    heapq.heappush(max_heap, -heapq.heappop(min_heap))

  if len(max_heap) > len(min_heap) + 1:
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

  # print(f"{number}: max heap : {list(-i for i in reversed(max_heap))}, min heap : {min_heap}")
  answer.append(str(-max_heap[0]))

sys.stdout.write("\n".join(answer) + "\n")