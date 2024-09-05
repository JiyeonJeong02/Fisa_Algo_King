## 진짜 너무 힘들다
## 그냥 최대 50개 밖에 안되니깐 하나하나 다 점검하는 걸로 했습니다.
## 그냥 완전탐색으로 했습니다.


# 데이터 입력
M, N = map(int, input().split())
ches = [list(input()) for _ in range(M)]


# min으로 답인지 아닌지를 조정할거기 때문에 초기값을 inf로 한다.
answer = float('inf')

for i in range(M - 7):
    for j in range(N - 7):  ## 최대가 8을 유지해야 하므로 7을 삭제
        count_b = 0  # 검정 시작
        count_w = 0  # 흰색 시작
        
        # 8x8 영역 체크
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # 검정색 시작
                if (x + y) % 2 == 0:
                    if ches[x][y] != 'B':
                        count_b += 1
                else: 
                    if ches[x][y] != 'W':
                        count_b += 1
        
        # 흰색 시작 패턴
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # 흰색 시작 패턴
                if (x + y) % 2 == 0: 
                    if ches[x][y] != 'W':
                        count_w += 1
                else:  
                    if ches[x][y] != 'B':
                        count_w += 1
        
        answer = min(answer, count_b, count_w)

print(answer)