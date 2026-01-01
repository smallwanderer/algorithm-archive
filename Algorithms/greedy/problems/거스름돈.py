"""
거스름돈 문제

거스름돈 문제는 주어진 금액을 특정 화폐 단위로 나누어 거슬러 주는 문제입니다.
이 문제는 동적 계획법(Dynamic Programming)을 사용하여 해결할 수 있습니다.
두 가지 변형이 있습니다:
1. 순서 상관 없이 거스름돈을 만드는 방법의 수를 구하는 문제
2. 순서 상관 있게 거스름돈을 만드는 방법의 수를 구하는 문제

1번의 경우, 화폐 단위의 순서가 중요하지 않으므로 각 화폐 단위를 한 번씩만 고려합니다.
즉, 화폐 단위의 종류별로 dp 배열을 갱신합니다. 1번 화폐 단위를 사용한다면, dp배열은 1번 화폐를 사용한 이후의 상태를 반영합니다.
이후 2번 화폐 단위를 사용하여 dp를 갱신할 때, dp는 이미 1번 화폐 단위를 사용하였음을 가정합니다. 
따라서, 1번 화폐 단위를 여러 번 사용하는 경우는 중복 계산되지 않습니다.

2번의 경우, 화폐 단위의 순서가 중요하므로 각 금액에 대해 모든 화폐 단위를 고려합니다.
즉, 각 화폐의 단위가 "마지막"으로 들어갔음을 가정합니다. dp[4]를 구할 때 마지막으로 1원을 사용하는 경우 dp[3]과 연결되고, 
마지막으로 2원을 사용하는 경우 dp[2]와 연결됩니다.
이 경우 dp[3]은 [1,1,1], [2,1] 두 가지 방법이 있고, dp[2]는 [1,1], [2] 두 가지 방법이 있으므로 dp[4]는 총 4가지 방법이 됩니다.
"""

# 순서 상관 없이 거스름돈을 만드는 방법의 수를 구하는 문제 
def dp_change_comb(n, money):
    # 거스름돈을 만드는 방법의 수를 저장하는 리스트
    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지 (아무것도 사용하지 않는 방법)
    
    for coin in reversed(money):
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]
            dp[amount] %= 1000000007  # 결과가 커질 수 있으므로 나머지 연산 수행
        print(f"DP after processing coin {coin}: {dp[1:]}")

    return dp[n]


# 순서 상관 있게 거스름돈을 만드는 방법의 수를 구하는 문제
def dp_change_perm(n, money):
    # 거스름돈을 만드는 방법의 수를 저장하는 리스트
    dp = [0] * (n + 1)
    dp[0] = 1

    for amount in range(1, n + 1):
        for coin in money:
            if amount - coin >= 0:
                dp[amount] += dp[amount - coin]
                dp[amount] %= 1000000007  # 결과가 커질 수 있으므로 나머지 연산 수행
        print(f"DP after processing amount {amount}: {dp[1:]}")
    return dp[n]

# 테스트 예시
if __name__ == "__main__":
    n = 10
    money = [1, 2, 5]
    print(dp_change_comb(n, money))  # 10

    print("-----")