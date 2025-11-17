import math
def solution(n, k):
  arr = list(range(1, n+1))

  def recursion_12936(arr, available, n, k):
    if len(arr) == n:
      return arr
    idx = (k-1)//math.factorial(len(available)-1)
    k -= idx * math.factorial(len(available)-1)
    arr.append(available.pop(idx))
    return recursion_12936(arr, available, n, k)

  return recursion_12936([], arr, n, k)