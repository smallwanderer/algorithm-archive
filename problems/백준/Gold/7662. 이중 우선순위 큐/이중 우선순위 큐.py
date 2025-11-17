import sys
import heapq
import collections

def sync(w, heap, numbers_count):
  if w == 1:
    while heap and numbers_count[-heap[0]] == 0:
      heapq.heappop(heap)
  else:
    while heap and numbers_count[heap[0]] == 0:
      heapq.heappop(heap)

def process_test_case():
    n = int(sys.stdin.readline().strip())
    min_heap, max_heap = [], []
    numbers_count = collections.defaultdict(int)
    cnt = 0

    for _ in range(n):
        op, val = sys.stdin.readline().strip().split()
        val = int(val)

        if op == 'I':
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
            numbers_count[val] += 1
            cnt += 1

        elif op == 'D':
            if cnt == 0:
                continue

            if val == 1:
                sync(1, max_heap, numbers_count)
                max_val = -heapq.heappop(max_heap)
                numbers_count[max_val] -= 1
            else:
                sync(2, min_heap, numbers_count)
                min_val = heapq.heappop(min_heap)
                numbers_count[min_val] -= 1
            cnt -= 1

    sync(2, min_heap, numbers_count)
    sync(1, max_heap, numbers_count)

    if cnt == 0:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])

t = int(sys.stdin.readline().strip())
for _ in range(t):
    process_test_case()
