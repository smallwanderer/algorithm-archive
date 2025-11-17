"""
휴리스틱 알고리즘(Heuristic Algorithm)
- 문제에 근사적인 해결책을 찾기 위해 경험적이고 규칙적인 방법을 제시합니다.
- 해당 방식은 최적해를 보장하지 않으며, 문제를 근사적이고 빠르게 도출해내는데 사용됩니다.
  1. 가지치기(Pruning)
  - 탐색 과정에서 필요없는 부분들을 무시하고 탐색하는 방식
"""
from typing import List, Tuple

class Heuristic_NQueen:
  """
  N-Queen:
  NxN의 체스판에서 최대의 queen을 둘 수 있는 해의 개수를 구하여야 합니다.
  NxN의 체스판에서 queen을 놓는 방법은 N개이다. (각 row에 하나의 queen을 둬야 함)

  - 각 row마다
  """
  def __init__(self, n=4, visualization=False):
    self.n = n
    self.placed = []
    self.coordinates = [] # 전체 해들의 좌표값
    self.visualization = visualization
    if visualization:
      self.visualizations = [] # 전체 해들의 상태를 저장
    self.cnt = 0

    self.used_rows = set()
    self.used_cols = set()
    self.used_d1 = set()
    self.used_d2 = set()

  def in_bounds(self, x, y):
    return 0 <= x < self.n and 0 <= y < self.n

  def c_free(self, x, y):
    if not self.in_bounds(x, y):
      return False
    if x in self.used_cols or y in self.used_rows:
      return False
    if (y-x) in self.used_d1 or (y+x) in self.used_d2:
      return False
    return True

  def place(self, x, y):
    if not self.in_bounds(x, y):
      return False, "Out of Bound"
    if not self.c_free(x, y):
      reason = (
        "col" if x in self.used_cols else
        "row" if y in self.used_rows else
        "diag1" if (y-x) in self.used_d1 else
        "diag2" if (y+x) in self.used_d2 else
        "blocked"
      )
      return False, reason

    self.used_rows.add(y)
    self.used_cols.add(x)
    self.used_d1.add((y-x))
    self.used_d2.add((y+x))
    self.placed.append((x, y))
    return True, "Placed OK"

  def unplace(self, x, y):
    if not self.in_bounds(x, y):
      return False, "Out of Bound"
    if (x, y) not in self.placed:
      return False, "Position Not Appropriate"

    self.used_rows.discard(y)
    self.used_cols.discard(x)
    self.used_d1.discard((y-x))
    self.used_d2.discard((y+x))
    self.placed.remove((x, y))
    return True, "Unplaced OK"

  def neighbor_node(self, row):
    return [c for c in range(self.n) if self.c_free(c, row)]

  def canonical_coord(self, solution: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """
    체스판의 중앙으로 좌표계의 중심점을 이동하여 계산 과정 간편화
    8방향에 대한 좌표 계산
    """
    mid = (self.n-1) / 2
    shifted_list = list((x-mid, mid-y) for x, y in solution)
    # normalized_list = [((x/mid)-1, 1-(y/mid)) for x, y in solution]

    def t0(x,y):  return (x, y)              # 0°
    def t90(x,y): return (y, -x)             # 90°
    def t180(x,y):return (-x, -y)            # 180°
    def t270(x,y):return (-y, x)             # 270°
    def mx(x,y):  return (x, -y)             # 상하 반사
    def my(x,y):  return (-x, y)             # 좌우 반사
    def md(x,y):  return (y, x)              # y=x 대칭
    def ma(x,y):  return (-y, -x)            # y=-x 대칭

    trans = (t0, t90, t180, t270, mx, my, md, ma)

    canonical_list = []
    for T in trans:
      canonical_list.append(tuple(sorted(T(x,y) for x,y in shifted_list)))
    return tuple(sorted(canonical_list))

  def candidate_coord_test(self):
    test_list = [[(r, c) for r in range(self.n)] for c in range(self.n)]
    for x in test_list:
      print(x)
    for a in map(self.candidate_coord, test_list):
      print(a)
    return

  def pruning(self, row):
    # Using DFS to Find Path Approximately
    n = self.n
    if row == n:
      self.cnt += 1
      self.coordinates.append(list(self.placed))
      if self.visualization:
        self.visualizations.append(self.board_str())
      return

    for col in range(n):
      if self.c_free(col, row):
        self.place(col, row)
        self.pruning(row+1)
        self.unplace(col, row)

  def pruning_stack(self):
    n = self.n
    stacks = []
    # Frame) ("PLACE", candidates, row, idx) : ("Unplace", x, y)
    #   PLACE/UNPLACE: queen의 적용할 상태를 나타냅니다
    #   candidates: row에서 적용할 열 번호들
    #   row: 현재 행
    #   idx: 다음에 시도할 candidate의 색인 번호
    # Frame) ("UNPLACE", col, row)
    #   # UNPLACE를 수행해야 합니다.
    stacks.append(("PLACE", self.neighbor_node(0), 0, 0))

    while stacks:
      frame = stacks.pop()

      # "UNPLACE" 상태 해결
      if frame[0] == "UNPLACE":
        col, row = frame[1], frame[2]
        ok, _ = self.unplace(col, row)
        if not ok:
          return "UNPLACE ERROR!"
        continue

      # "PLACE" 상태 해결
      _, cands, row, idx = frame

      # 종료조건: 현재 행이 마지막 행인 경우
      if row == n:
        self.cnt += 1
        continue

      # Pruning: 해당 행에서 더이상 시도할 후보가 없는 경우
      if idx >= len(cands):
        continue

      # 현재 후보의 다음 후보를 시도하도록
      stacks.append(("PLACE", cands, row, idx+1))

      col = cands[idx]
      ok, _ = self.place(col, row)
      if not ok:
        continue

      stacks.append(("UNPLACE", col, row))
      stacks.append(("PLACE", self.neighbor_node(row+1) if row+1 < n else [], row+1, 0))

    return self.cnt


  def board_str(self) -> str:
    """
    Returns
    -------
    현재 상태에 대한 체스판 전체 상태를 시각화합니다.
    선언할 때 마다 체스판 전체를 새로 구성합니다!
    """
    symbol = {True: '.', False: 'x'}
    n = self.n
    chess = [[True for _ in range(n)] for _ in range(n)]

    for y in range(n):
      for x in range(n):
        if self.c_free(y, x):
          continue
        chess[y][x] = False

    for px, py in self.placed:
      chess[py][px] = 'q'

    return "\n".join(" ".join(symbol.get(c, c) for c in row) for row in chess) + "\n" + "-" * (self.n * 2)


if __name__ == "__main__":
  N = 12
  h1 = Heuristic_NQueen(n=N, visualization=False)
  h1.pruning(0)
  print("distinct:", h1.cnt)
  # for vis in h1.visualizations:
  #   print(vis)
  # for idx, coord in enumerate(h1.coordinates):
  #   print(idx, ':', coord)

  test_set = set()
  for idx, sol in enumerate(h1.coordinates):
    canon = h1.canonical_coord(sol)  # ← 반드시 tuple of tuples 반환
    test_set.add(canon)

  print("Unique:", len(test_set))