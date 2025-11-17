def solution(info, n, m):
    dp = set()
    dp.add((0, 0))

    for a_val, b_val in info:
        next_dp = set()
        for a_sum, b_sum in dp:
            if a_sum + a_val < n:
                next_dp.add((a_sum + a_val, b_sum))
            if b_sum + b_val < m:
                next_dp.add((a_sum, b_sum + b_val))
        dp = next_dp

    if not dp:
        return -1
    return min(a for a, _ in dp)
