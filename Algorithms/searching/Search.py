# 탐색 알고리즘
import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

class HashTable:
  def __init__(self, size):
    self.size = size
    self.table = [None] * size

  def _hash_func(self, key):
    return key % self.size

  def insert(self, key, value):
    idx = self._hash_func(key)
    start_idx = idx
    while self.table[idx] is not None:
      if self.table[idx][0] == key:      # 이미 같은 값이 저장되어 있음
        return
      idx = (idx+1) % self.size
      if idx == start_idx:                  # 해시 테이블이 모두 찬 경우
        raise Exception("Hash Table Full")
    self.table[idx] = (key, value)

  def search(self, key):
    idx = self._hash_func(key)
    start_idx = idx
    while self.table[idx] is not None:
      if self.table[idx][0] == key:
        return self.table[idx][1]
      idx = (idx+1) % self.size
      if idx == start_idx:
        break
    return None


class Search:
  def __init__(self, arr):
    self.arr = arr          # 탐색하는 배열
    self.size = len(arr)    # 배열의 크기
    self.operation_cnt = []  # 비교 연산 횟수

  def reset(self):
    self.operation_cnt = []

  def average_operation(self):
    if not self.operation_cnt:
      return 0
    return sum(self.operation_cnt) / len(self.operation_cnt)


  def linear_Search(self, key, low=0, high=None):
    if high is None:
      high = self.size
    cnt = 0

    for i in range(low, high):
      cnt += 1
      if self.arr[i] == key:
        self.operation_cnt.append(cnt)
        return i
    return -1

  def binary_Search(self, key, low=0, high=None):
    if high is None:
      high = self.size
    cnt = 0

    sorted_subarr = sorted(self.arr[low:high])
    left, right = 0, high - low - 1

    while left <= right:
      cnt += 1
      mid = (left + right) // 2
      mid_val = sorted_subarr[mid]

      if mid_val == key:
        self.operation_cnt.append(cnt)
        return mid + low
      elif mid_val < key:
        left = mid + 1
      else:
        right = mid - 1
    self.operation_cnt.append(cnt)
    return -1

  def interpolation_Search(self, key, low=0, high=None):
    if high is None:
      high = self.size
    cnt = 0

    sorted_subarr = sorted(self.arr[low:high])
    left, right = 0, high - low - 1

    while left <= right and sorted_subarr[left] <= key <= sorted_subarr[right]:
      cnt += 1

      pos = left + ((right - left) * (key - sorted_subarr[left])) // \
            (sorted_subarr[right] - sorted_subarr[left])

      if pos < 0 or pos >= len(sorted_subarr):
        break

      if sorted_subarr[pos] == key:
        self.operation_cnt.append(cnt)
        return pos + low
      elif sorted_subarr[pos] < key:
        left = pos + 1
      else:
        right = pos - 1
    self.operation_cnt.append(cnt)
    return -1


def run_experiment(search_class, search_method, n, jump, array_size, dist="uniform"):
  avg_ops = []
  for num_trial in range(jump, n, jump):
    if dist == "uniform":
      arr = [random.randint(0, array_size) for _ in range(array_size)]
    elif dist == "skewed":
      arr = [int((random.random() ** 2) * array_size) for _ in range(array_size)]
    else:
      raise ValueError("Invalid distribution type. Use 'uniform' or 'skewed'.")

    searcher = search_class(arr)
    for _ in range(num_trial):
      key = random.randint(0, array_size)
      getattr(searcher, search_method)(key)
    avg_ops.append(searcher.average_operation())
  return avg_ops

if __name__ == "__main__":

  # print("====HASH====")
  # ht = HashTable(10)
  # ht.insert(123, "apple")
  # ht.insert(172, 'pear')
  # ht.insert(111, 'tangerine')
  # print(ht.search(111))

  n = 1000
  array_size = 100
  jump = 20

  results = run_experiment(Search, "interpolation_Search", n, jump, array_size, dist='uniform')

  X = np.array(range(jump, n, jump)).reshape(-1, 1)
  y = np.array(results)
  model = LinearRegression().fit(X, y)
  y_pred = model.predict(X)

  plt.scatter(range(jump, n, jump), results, color='blue')
  plt.plot(range(jump, n, jump), y_pred, color='red')
  plt.title("Comparison of Search algorithms by number of trials (Interpolation Search)")
  plt.xlabel("trial")
  plt.ylabel("%")
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()



  

