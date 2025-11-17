def paperFold(paper):
  if len(paper)==1:
    return "YES"
  if paperValid(paper):
    return paperFold(paper[:len(paper)//2])
  else:
    return "NO"

def paperValid(paper_list):
  length = len(paper_list)
  for idx in range(length//2):
    if paper_list[idx] == paper_list[length-1-idx]:
      return False
  return True

T = int(input())
result = []
for i in range(T):
  folded_paper = input()
  result.append(paperFold(folded_paper))

for i in result:
  print(i)