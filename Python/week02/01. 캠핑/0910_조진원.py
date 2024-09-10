

i = 0  # 넘버링 시작
answer_list = [] # 정답 리스트 생성


while True : # 무한반복 시작
    L, P, V = map(int, input().split())
    if (L == 0) & (P == 0) & (V == 0) : # 입력값이 0이면 종료
        break
    i += 1 # 넘버링
    answer = V // P * L + min(V % P, L)  # 정답 생성
    answer_list.append(f'Case {i}: {answer}')

for i in answer_list : # 정답값 출력
    print(i)