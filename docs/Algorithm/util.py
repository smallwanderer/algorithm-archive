import math
from typing import Iterable, Tuple, List

# 직교 좌표(x, y)를 극좌표(r, theta)로 변환
def cart2polar(x: float, y:float) -> Tuple[float, float]:
  r = math.hypot(x, y)
  # atan(-pi/2 ~ pi/2)은 방향이 없는 두 좌표의 각도
  theta = 0.0 if r == 0.0 else math.atan2(y, x) #(-pi ~ pi)

  return r, theta

# 극좌표 (r, theta)를 직교좌표계로 변환
def polar2cart(r:float, theta:float) -> Tuple[float, float]:
  return r * math.cos(theta), r * math.sin(theta)

# theta를 [0, 2pi)로 변환
def norm_angle_0_2pi(theta: float) -> float:
  twopi = 2.0 * math.pi
  return ((theta % twopi) + twopi) % twopi

def batch_cart2polar(points: Iterable[Tuple[float, float]],
                     normalize: bool = False) -> List[Tuple[float, float]]:
  batch_polars = []
  for x, y in points:
    r, th = cart2polar(x, y)
    batch_polars.append((r, norm_angle_0_2pi(th) if normalize else th))

  return batch_polars