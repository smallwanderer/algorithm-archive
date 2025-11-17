import collections
def sliding_window_12891(arr, sub_len, rule):
  # 주어진 문자열에서 만들 수 있는 부분 문자열의 개수를 계산
  a_counter = collections.Counter(arr[:sub_len])

  def is_Valid_12891(a_counter, rule) -> int:
    for r_item, r_val in rule.items():
      if a_counter.get(r_item, 0) < r_val:
        return 0
    return 1

  cnt = is_Valid_12891(a_counter, rule)
  for p1 in range(len(arr) - sub_len):
    a_counter[arr[p1]] -= 1
    a_counter[arr[p1+sub_len]] = a_counter.get(arr[p1+sub_len], 0) + 1
    cnt += is_Valid_12891(a_counter, rule)

  return cnt

string_length, substring_length = map(int, input().split())
strings = input()
rule = list(map(int, input().split()))
rule = {'A': rule[0], 'C': rule[1], 'G': rule[2], 'T': rule[3]}
print(sliding_window_12891(strings,substring_length,rule))