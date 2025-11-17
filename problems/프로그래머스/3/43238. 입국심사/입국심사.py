def solution(n, times):
    left, right = 0, n * max(times)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)

        # total = n 이 되는 범위 (28 ~ 29)

        total = sum(mid // t for t in times)
        if total < n:
            left = mid + 1
            answer = left
        else:
            right = mid - 1
            
    print(left, mid, right)
    return answer