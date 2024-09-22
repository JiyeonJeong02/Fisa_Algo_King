from collections import Counter

st = input()
str_cnt = dict(Counter(st))
str_cnt = dict(sorted(str_cnt.items())) #알파벳 순으로 정렬
answer = []
values = list(str_cnt.values())
keys = list(str_cnt.keys())
sum_iters = 0

#len(st)가 짝수인 경우
if len(st) % 2 == 0:
    for idx in range(len(values)):
        if values[idx] % 2 == 0:
            iters = values[idx] // 2
            sum_iters += iters
            answer.append((keys[idx], iters))
        else :
            break

    if sum_iters == len(st) // 2:
        final_answer = ''
        for i in range(len(answer)):
            final_answer += answer[i][0]* answer[i][1]

        print(final_answer+final_answer[::-1])
    else:
        print("I'm Sorry Hansoo")


else:
    odd_cnt = 0
    odd = ''
    for idx in range(len(values)):
        if values[idx] % 2 == 0:
            iters = values[idx] // 2
            sum_iters += iters
            answer.append((keys[idx], iters))
        elif (odd_cnt == 0) and (values[idx] % 2 == 1): #홀수는 한 번만 등장 가능
            odd_cnt += 1
            odd += keys[idx]
            iters = values[idx] // 2
            sum_iters += iters
            answer.append((keys[idx], iters))
        else:
            break

    if sum_iters + 1 == len(st) // 2 + 1:
        final_answer = ''
        for i in range(len(answer)):
            final_answer += answer[i][0]* answer[i][1]
        print(final_answer+odd+final_answer[::-1])
    else:
        print("I'm Sorry Hansoo")