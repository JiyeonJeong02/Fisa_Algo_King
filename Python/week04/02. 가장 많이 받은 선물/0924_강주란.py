#선물을 가장 많이 받을 친구가 받을 선물의 수 구하기

def solution(friends, gifts):
    n = len(friends)
    gift_matrix = [[0 for i in range(n)] for i in range(n)]
    scores = dict(zip(friends, [0]* n))
    gift_num = [0 for i in range(n)]
    for i in range(len(gifts)):
        giver, taker = gifts[i].split(' ')
        if giver in friends:
            scores[giver] += 1
        if taker in friends:
            scores[taker] -= 1

        giver_idx = friends.index(giver)
        taker_idx = friends.index(taker)
        gift_matrix[giver_idx][taker_idx] += 1


    for i in range(n): #준 사람
        for j in range(n): #받는 사람
            if gift_matrix[i][j] > gift_matrix[j][i]: #더 많이 준 경우
                gift_num[i] += 1
            elif gift_matrix[i][j] < gift_matrix[j][i]: #적게 준 경우
                pass
            else: #gift_matrix[i][j] == gift_matrix[i][j] # 같은 경우 or 주고받지 않은 경우
                if scores[friends[i]] > scores[friends[j]]:
                    gift_num[i] += 1
                else:
                    pass
    answer = max(gift_num)
    return answer