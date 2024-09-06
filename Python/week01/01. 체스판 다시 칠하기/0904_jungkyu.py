### 풀이시간 ###
# 19:10~20:10 (1시간)

### 접근 방식 ###
# 색깔로 된 타일을 체스판의 논리에 맞게 1, 0로 재구성
# 첫칸이 Black 일때, white 일때 나누어서 생각

import sys

N, M = list(map(int, input().split()))

### 체크보드 세팅
check_board = [[0] * M for _ in range(N)]

for i in range(N):
    line = sys.stdin.readline()
    if i % 2 == 0:
        for j in range(M):
            if j % 2 == 0:
                if line[j] == 'B':
                    check_board[i][j] = 1
                else:
                    check_board[i][j] = 0
            else:
                if line[j] == 'W':
                    check_board[i][j] = 1
                else:
                    check_board[i][j] = 0
    else:
        for j in range(M):
            if j % 2 == 0:
                if line[j] == 'W':
                    check_board[i][j] = 1
                else:
                    check_board[i][j] = 0
            else:
                if line[j] == 'B':
                    check_board[i][j] = 1
                else:
                    check_board[i][j] = 0

### 정답 도출
ans = 100

for i in range(N - 7):
    for j in range(M - 7):
        # 2차원 배열 슬라이싱 방식 (찾은 부분)
        select_board = [row[j:j+8] for row in check_board[i:i+8]]

        # 2차원 배열 sum 방식
        change_total = sum(sum(select_board, []))

        # 64 - change_total 는 첫칸이 흰색이 정답일 때
        ans = min(ans, change_total, 64 - change_total)

        # 정답으로 나올 수 있는 최소값는 0이므로 스탑!
        if ans == 0:
            break

print(ans)