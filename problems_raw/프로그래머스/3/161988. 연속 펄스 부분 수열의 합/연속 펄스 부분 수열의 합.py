def solution(sequence):
  neg_dp, pos_dp = 0, 0
  kadane_sum = -float("inf")
  pulse = -1
  for num in sequence:
    neg_dp = max(num*pulse + neg_dp, num*pulse)
    pos_dp = max(num*(-pulse) + pos_dp, num*(-pulse))
    kadane_sum = max(kadane_sum, neg_dp, pos_dp)
    pulse *= -1
  return kadane_sum