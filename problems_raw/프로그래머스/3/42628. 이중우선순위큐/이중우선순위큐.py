def solution(operation):
  answer = set([])
  for op in operation:
    if op[0] == 'I':
      answer.add(int(op[2:]))
    else:
      if len(answer) == 0:
        continue
      if op[2] == '-':
        answer.remove(min(answer))
      else:
        answer.remove(max(answer))
  return [max(answer), min(answer)] if len(answer) != 0 else [0, 0]