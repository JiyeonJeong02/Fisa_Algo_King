### 공부 시간 ###
# 14:10 ~ 15:50, 13:10 ~ 14:50 (3시간 20분)

### 접근 방식 ###
# 인간관계 최소경로를 구해야한다.
# 그래프 그려서 BFS 로 자기자신 외 나머지 사람까지 도달하는 데 최소 경로의 합을 구한다.
# 큐를 사용하여 구현

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 그래프 설정
adj = [[0] * (N + 1) for _ in range(N + 1)]

# 1 -> 2 가는 것과 2 -> 1 가는 짧은 거리는 똑같다
# 중복 연산을 피하기 위해 한번 계산 한것은 저장
store = [[-1] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    friend_one, friend_two = map(int, input().split())
    adj[friend_one][friend_two] = adj[friend_two][friend_one] = 1

def bfs(start, end):
    # 방문여부
    if store[start][end] != -1:
        return store[start][end]

    dq = deque()
    dq.append((start, 0))  # 위치와 방문 횟수를 저장
    chk = [False] * (N + 1)  # chk 리스트를 bfs 내부로 이동하여 초기화
    chk[start] = True  # 시작점을 방문 처리

    while dq:
        now, dist = dq.popleft()

        if now == end:
            store[start][end] = store[end][start] = dist
            return dist

        for nxt in range(1, N + 1):
            if adj[now][nxt] and not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, dist + 1))

    return 10000

# 최소값 뽑을 리스트
ans = {}

for j in range(1, N + 1):
    case_list = []
    for k in range(1, N + 1):
        if j != k:
            case_one = bfs(j, k)
            case_list.append(case_one)
    ans[j] = sum(case_list)

# 딕셔너리 최소값 가진 키값 출력
print(min(ans, key=ans.get))
