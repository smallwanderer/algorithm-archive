# sorting algorithm 모음
import math
import time

class Sort:
  def __init__(self, arr):
    self.arr = arr
    self.operation_cnt = 0

  def selectionSort(self):
    unsortedArr = self.arr[:]

    print("selection sort operation count : ", end="")
    self.operation_cnt = 0

    for i in range(len(unsortedArr)):
      minimumEntity = (unsortedArr[i], i)    # 정렬 되지 않은 배열의 최소값과 그 인덱스
      for j in range(i, len(unsortedArr)):
        if unsortedArr[j] < minimumEntity[0]:
          minimumEntity = (unsortedArr[j], j)
        self.operation_cnt += 1
      unsortedArr[minimumEntity[1]] = unsortedArr[i]
      unsortedArr[i] = minimumEntity[0]

    print(self.operation_cnt)
    return unsortedArr

  def insertionSort(self):
    unsortedArr = self.arr[:]

    print("insertion sort operation count : ", end="")
    self.operation_cnt = 0

    for idx in range(1, len(unsortedArr)):
      current = unsortedArr[idx]
      previous_idx = idx-1

      while unsortedArr[previous_idx] > current and previous_idx >= 0:
        unsortedArr[previous_idx+1] = unsortedArr[previous_idx]
        previous_idx -= 1
        self.operation_cnt += 1
      unsortedArr[previous_idx+1] = current

    print(self.operation_cnt)
    return unsortedArr

  def bubbleSort(self):
    unsortedArr = self.arr[:]

    print("bubble sort operation count : ", end="")
    self.operation_cnt = 0

    for times in range(len(unsortedArr)):
      for idx in range(len(unsortedArr)-times-1):
        temp = unsortedArr[idx]
        if unsortedArr[idx+1] < temp:
          unsortedArr[idx] = unsortedArr[idx+1]
          unsortedArr[idx+1] = temp
          self.operation_cnt += 1

    print(self.operation_cnt)
    return unsortedArr




if __name__ == '__main__':
  import random

  arr = [random.randint(0, 10) for _ in range(10)]
  print(*arr)

  sort = Sort(arr)
  print(*sort.selectionSort())
  print(*sort.insertionSort())
  print(*sort.bubbleSort())



