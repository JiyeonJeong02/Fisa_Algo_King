### 풀이시간 ###
# 13:15 ~ 14:15 (1시간)

### 접근 방식 ###
# 여러 치킨집 중에 살려야할 치킨집을 골라야하므로 조합을 사용해서 케이스 나누기
# 각각 케이스 마다 집에서 치킨집까지 거리 계산해서 비교
# 거리 계산 방식은 문제에 나온대로...

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

home_list = []
chicken_list = []

## 치킨집과 집 위치 파악
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home_list.append((i, j))
        elif board[i][j] == 2:
            chicken_list.append((i, j))

## 케이스별 거리 총합 기록해서 최소값 뽑을 리스트
ans = []

## 남겨지는 치킨집에 따라 최소 경로 계산
for chicken_case in combinations(chicken_list, M):
    case_lengths = []

    ## 집별로 치킨집으로 최소 거리 계산 필요
    for home_case in home_list:
        my_short = [] # 치킨집 별 거리 저장해서 최소값 뽑을 리스트

        for one_chicken in chicken_case:
            vs_length = abs(home_case[0] - one_chicken[0]) + abs(home_case[1] - one_chicken[1])
            my_short.append(vs_length)

        case_lengths.append(min(my_short))

    ans.append(sum(case_lengths))

print(min(ans))