#스택 - list : append, pop 이용

def solution(board, moves):
    answer = 0
    bucket = []
    n = len(board)
    test=[[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            test[col][n-1-row] = board[row][col]

    for move in moves:
        while len(test[move-1]) > 0:
            num = test[move-1].pop()
            if num == 0:
                pass
            else :
                bucket.append(num)
                break
        if (len(bucket)>1) and (bucket[-1] == bucket[-2]):
            bucket.pop()
            bucket.pop()
            answer += 1
    return answer*2






board = [[0,0,0,0,0]
         ,[0,0,1,0,3]
         ,[0,2,5,0,1]
         ,[4,2,4,4,2]
         ,[3,5,1,3,1]]

len(board)

test=[[0 for _ in range(5)] for _ in range(5)]
answer = 0

for row in range(5):
    for col in range(5):
        test[col][4-row] = board[row][col]


bucket = []
moves = [1,5,3,5,1,2,1,4]
for move in moves:
    while len(test[move-1]) > 0:
        num = test[move-1].pop()
        if num == 0:
            pass
        else :
            bucket.append(num)
            break
    if (len(bucket)>1) and (bucket[-1] == bucket[-2]):
        bucket.pop()
        bucket.pop()
        answer += 1

print(answer*2)

