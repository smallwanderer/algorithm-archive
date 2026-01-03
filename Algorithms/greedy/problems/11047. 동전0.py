"""
Docstring for Algorithms.greedy.problems.동전0
동전 0 문제

동전 0 문제는 주어진 금액을 최소한의 동전 개수로 거슬러 주는 문제입니다.
이 문제는 그리디 알고리즘(Greedy Algorithm)을 사용하여 해결할 수 있습니다.
"""

import sys
input = sys.stdin.readline

def greedy_coin_change(n, coins):
    # 동전 단위를 내림차순으로 정렬
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if n == 0:
            break
        count += n // coin
        n %= coin
        
    return count

# 테스트 예시
if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    coins = [int(input().strip()) for _ in range(n)]
    print(greedy_coin_change(k, coins))
