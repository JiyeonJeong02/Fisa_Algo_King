def solution(survey, choices):
    score = 0
    type = ''
    answer = ''
    type_dic = dict(zip(["R", "T", "C", "F", "J", "M", "A", "N"], [0]*8))

    for choice, sur in zip(choices, survey):
        if choice in [1,2,3]:
            type = sur[0]
        elif choice in [5,6,7]:
            type = sur[1]
        else:
            type = sur[0] #안적으면 에러..


        if choice in [1, 7]:
            score = 3
        elif choice in [2, 6]:
            score = 2
        elif choice in [3, 5]:
            score = 1
        else:
            score = 0

        type_dic[type] += score


    for i in range(4):
        char, score = sorted(list(type_dic.items())[(2*i):(2*i)+2], key=lambda x : (x[1], -ord(x[0])))[1]
        answer += char

    return answer