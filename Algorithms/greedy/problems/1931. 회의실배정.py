"""
회의실 배정

각 회의마다 시작 시간과 끝나는 시간이 주어져 있을 때, 최대한 많이 회의를 하는 수
"""

import sys
input = sys.stdin.readline

def greedy_meeting_schedule(meetings):
    # 회의를 끝나는 시간 기준으로 정렬, 끝나는 시간이 같으면 시작 시간 기준으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    count = 0
    end_time = 0

    for start, end in meetings:
        if start >= end_time:
            count += 1
            end_time = end
    
    return count

# 테스트 예시
if __name__ == "__main__":
    n = int(input().strip())
    meetings = [tuple(map(int, input().strip().split())) for _ in range(n)]

    print(greedy_meeting_schedule(meetings))    