### 풀이시간 ###
# 16:52 ~ 17:22 (30분)

### 접근 방식 ###
# 1. 총 휴가 기간 V 에서 P 만큼 나누었을 때 몇 구간이 나오는 지 판단
# 2. 구간마다 사용할 수 있는 일수는 L 일이다.
# 3. 마지막 구간의 일수가 L일 보다 짧을 경우 나머지를 더하고, L일 보다 길거나 같을 경우 L일 더한다.

import sys

input = sys.stdin.readline

i = 1
input_dict = {}

while True:
    L, P, V = map(int, input().split())
    if (L == 0) and (P == 0) and (V == 0):
        break
    input_dict[i] = [L, P, V]

    i += 1

for key, value in input_dict.items():
    L = value[0]
    P = value[1]
    V = value[2]

    seq = int(V // P)
    last_seq = int(V % P)

    if last_seq < L:
        ans = (seq * L) + last_seq
    else:
        ans = (seq * L) + L

    print(f'Case {key}: {ans}')
