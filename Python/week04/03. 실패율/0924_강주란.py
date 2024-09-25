# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

from collections import Counter
def solution(N, stages):
    stages_cnt = Counter(stages)
    failures = []
    denominator = len(stages)
    for i in range(1, N+1):
        if denominator > 0: #예외처리!!
            failures.append(stages_cnt[i]/denominator)
            denominator -= stages_cnt[i]
        else:
            failures.append(0)

    answer= [i+1 for i, v in sorted(enumerate(failures), key=lambda x:x[1], reverse = True)]
    return answer
###################################################
#stage1
1/8

#stage2
3/7

#stage3
2/4

#stage4
1/2

#stage5
0
