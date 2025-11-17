import collections

def distribute_reduce(n, num, num_count):
  base_reduce = n // num_count
  extra_reduce = n % num_count
    
  if num-base_reduce < 0:
    return 0

  result = [num-base_reduce] * num_count

  for i in range(extra_reduce):
    result[i] -= 1
    if result[i] < 0:
      return 0

  return sum(x*x for x in result)

def solution(n, work):
  work_dict = dict(collections.Counter(work))
  numbers = sorted(work_dict.keys(), reverse=True)
  cnt = n
  max_idx = 0
  result = 0
  while cnt != 0:
    max_num, val = numbers[max_idx], work_dict[numbers[max_idx]]
    next_num = numbers[max_idx+1] if max_idx+1 < len(numbers) else numbers[max_idx]

    if max_num == next_num:
      return distribute_reduce(cnt, max_num, val)

    reach_val = (max_num - next_num)
    if cnt < reach_val * val:
      result += distribute_reduce(cnt, max_num, val)
      work_dict[max_num] = 0
      break

    numbers.pop(0)
    work_dict[max_num] = 0
    work_dict[next_num] += val
    cnt -= reach_val * val

  result += sum(x*x*y for x, y in work_dict.items())
  return result