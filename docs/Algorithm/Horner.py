from __future__ import annotations
from typing import List, Tuple
import random, time, timeit, tracemalloc, gc, statistics, math

class Polynomial:
  """Polynomial evaluator (naive exponent-based evaluation).

  Evaluates a polynomial defined by its coefficients:
  a_0, a_1, ..., a_{n-1}  where index i corresponds to x^i.

  Example:
    coefficients = [a0, a1, a2] represents: a0 + a1*x + a2*x^2

  Methods in this class use a straightforward power accumulation method (not Horner's method).
  """

  def compute_polynomial(self, coefficients: List[float], x: float) -> float:
    """Compute polynomial value using naive summation of a_i * x^i.

    Args:
      coefficients (List[float]): Coefficients where coefficients[i] is the
        multiplier for x^i. Length n means degree up to n-1.
      x (float): Evaluation point.

    Returns:
      float: The evaluated value of the polynomial at x.
    """
    result = 0.0
    n = len(coefficients)

    for i in range(n-1, -1, -1):
      result += coefficients[i] * pow(x, i)

    return result


class Horner:
  """Horner's method based polynomial evaluator.

  This class intends to evaluate the same polynomial using Horner's scheme:
    (((a_{n-1})*x + a_{n-2})*x + ... + a_1)*x + a_0
  """

  def compute_polynomial(self, coefficients: List[float], x: float) -> float:
    """Compute polynomial value using Horner's method.

    Args:
      coefficients (List[float]): Coefficients where coefficients[i] maps to x^i.
      x (float): Evaluation point.

    Returns:
      float: The evaluated value.
    """
    n = len(coefficients)
    if n == 0:
      return 0.0
    result = float(coefficients[-1])

    for i in range(n-2, -1, -1):
      result = result * x + coefficients[i]

    return result


# ====== 1) 로직 검증(오류 시 즉시 중단) ======
def validate_correctness() -> None:
  """Check both evaluators on known cases and randomized inputs; abort on fail."""
  poly = Polynomial()
  horn = Horner()

  # Known small polynomials
  cases: List[Tuple[List[float], float]] = [
      ([1.0], 2.0),                 # a0
      ([1.0, 1.0], 2.0),            # a0 + a1*x
      ([0.0, 1.0, 1.0], 3.0),       # a1*x + a2*x^2
      ([2.0, -1.0, 0.5], 1.25),     # mix
  ]
  for coeffs, x in cases:
    a = poly.compute_polynomial(coeffs, x)
    b = horn.compute_polynomial(coeffs, x)
    assert math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12), f"Mismatch: {a} vs {b}"

  # Randomized tests
  random.seed(42)
  for _ in range(200):
    n = random.choice([4, 8, 16, 32, 64])
    coeffs = [random.uniform(-1.0, 1.0) for _ in range(n)]
    x = random.uniform(0.5, 1.5)
    a = poly.compute_polynomial(coeffs, x)
    b = horn.compute_polynomial(coeffs, x)
    assert math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12), "Randomized mismatch"

# ====== 2) 시간 벤치마크 ======
def bench_time(coeffs: List[float], x: float, repeats: int = 10000) -> Tuple[float, float]:
  """Return (naive_ms, horner_ms) average latency per call in milliseconds."""
  poly = Polynomial()
  horn = Horner()

  # Warm-up
  for _ in range(200):
    poly.compute_polynomial(coeffs, x)
    horn.compute_polynomial(coeffs, x)

  gc.collect()
  t_poly = timeit.timeit(lambda: poly.compute_polynomial(coeffs, x), number=repeats)
  gc.collect()
  t_horn = timeit.timeit(lambda: horn.compute_polynomial(coeffs, x), number=repeats)

  return (t_poly * 1000 / repeats, t_horn * 1000 / repeats)

# ====== 3) 메모리 벤치마크 ======
def bench_memory(n: int, batch: int = 200_000_000) -> Tuple[float, float]:
  """Return peak memory (MiB) for bulk evals: (naive_peak, horner_peak)."""
  coeffs = [random.uniform(-1.0, 1.0) for _ in range(n)]
  xs = [1.001 + (i % 5) * 0.0001 for i in range(batch)]  # deterministic small variation
  poly = Polynomial()
  horn = Horner()

  # Naive
  gc.collect()
  tracemalloc.start()
  for x in xs:
    poly.compute_polynomial(coeffs, x)
  _, peak_naive = tracemalloc.get_traced_memory()
  tracemalloc.stop()

  # Horner
  gc.collect()
  tracemalloc.start()
  for x in xs:
    horn.compute_polynomial(coeffs, x)
  _, peak_horner = tracemalloc.get_traced_memory()
  tracemalloc.stop()

  MiB = 1024 * 1024
  return (peak_naive / MiB, peak_horner / MiB)

def main():
  # 1) 정확성 검증
  try:
    validate_correctness()
  except AssertionError as e:
    print("❌ Logic error detected. Stop benchmarking.")
    print(f"Reason: {e}")
    return

  # 2) 시간 벤치마크(여러 n/x에 대해)
  print("=== Time Benchmark (ms per call) ===")
  ns = [4, 8, 16, 32, 64, 128, 256, 512]
  for n in ns:
    coeffs = [random.uniform(-1.0, 1.0) for _ in range(n)]
    xs = [1.001, 0.9, 1.2]
    for x in xs:
      naive_ms, horner_ms = bench_time(coeffs, x, repeats=10000 if n <= 128 else 3000)
      print(f"n={n:>3}, x={x:.3f}  |  naive={naive_ms:>7.3f} ms   horner={horner_ms:>7.3f} ms")

  # 3) 메모리 벤치마크(대표 n에서 피크 비교)
  print("\n=== Memory Benchmark (peak MiB) ===")
  for n in [64, 256, 512]:
    naive_peak, horner_peak = bench_memory(n, batch=80_000 if n>=256 else 200_000)
    print(f"n={n:>3}  |  naive_peak={naive_peak:6.2f} MiB   horner_peak={horner_peak:6.2f} MiB")

if __name__ == "__main__":
  main()