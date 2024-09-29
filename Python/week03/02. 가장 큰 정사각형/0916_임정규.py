### 풀이 시간 ###
# 15:10 ~ 15:45 (35분)

### 접근 방식 ###
# 주어진 보드에서 제일 큰 단위의 정사각형부터 서치
# 크기를 줄여가며 정사각형이 있는 지 체크
# 영역의 합이 원하는 크기와 일치하는 지 비교하면서 서치
## 시간초과

# 다 탐색을 하는 것이 아닌 왼쪽 상단 꼭지점으로 부터 만들수 있는 정사각형의 최대 크기를 계산


import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []

# 보드 세팅
for _ in range(N):
    input_line = input()
    one_line = []
    for i in range(M):
        one_line.append(int(input_line[i]))
    board.append(one_line)

# 서치
ans = 0
max_length = min(N, M)

def search_square(select_length):
    for i in range(N - select_length + 1):
        for j in range(M - select_length + 1):
            select_square = [row[j:j+select_length] for row in board[i:i+select_length]]
            ans = sum(sum(select_square, []))
            if ans == select_length ** 2:
                return ans
    return -1

## 답안
for k in range(max_length, 0, -1):
    ans = search_square(k)
    if ans != -1:
        print(ans)
        break
