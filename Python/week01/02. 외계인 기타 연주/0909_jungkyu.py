### 풀이시간 ###
# 17:38 ~ 18:55 (1시간 17분)

### 접근 방식 ###
# 스택을 줄 수만큼 생성
# 플랫은 순서대로 눌러지므로, 입력이 들어오면 스택의 머리와 비교한다.
# 스택의 머리보다 작은 플랫을 눌러야 하면 같은 플랫이 나오거나 더 작은 플랫이 나올 때까지 pop()
# 스택의 머리보다 큰 플랫은 append(1)
# 스택의 자료가 더해지거나 빠질때 Count

import sys

N, M = list(map(int, input().split()))

flat = {}

for i in range(M + 1):
    flat[i] = []

ans = 0

for j in range(N):
    flat_idx, finger_idx = list(map(int, sys.stdin.readline().split()))

    if len(flat[flat_idx]) == 0 or flat[flat_idx][-1] < finger_idx:
        flat[flat_idx].append(finger_idx)
        ans += 1

    elif flat[flat_idx][-1] > finger_idx:

        while True:
            if len(flat[flat_idx]) == 0:
                flat[flat_idx].append(finger_idx)
                ans += 1
                break

            if flat[flat_idx][-1] > finger_idx:
                flat[flat_idx].pop()
                ans += 1
            elif flat[flat_idx][-1] == finger_idx:
                break
            else:
                flat[flat_idx].append(finger_idx)
                ans += 1
                break

print(ans)