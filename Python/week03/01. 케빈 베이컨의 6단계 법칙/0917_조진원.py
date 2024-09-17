import sys 
input = sys.stdin.readline  # 요거 안하니깐 백준에서 시간초과 뜸

N, M = map(int, input().split())
kevin = [[0] * M for _ in range(M)]

for _ in range(M) :
    x, y = map(int,input().split())
    kevin[x-1][y-1] = kevin[y-1][x-1] = 1


from collections import deque

def bfs(matrix, start, end) :
    edge = 0
    visited = [False] * N
    queue = deque([(start,edge)])

    while queue :
        (node, edge) = queue.popleft()
        visited[node] = True

        if node == end :
            break

        edge += 1
        for i in range(N) :
            if matrix[node][i] == 1 and not visited[i] :
                queue.append((i, edge))
    return edge


answer = dict()
for i in range(N) :
    answer[i] = 0
    for j in range(i+1, i+N) :
        answer[i] += bfs(kevin, i, j%N)


# print(min(answer.items(), key=lambda x: (x[1], x[0]))[0] + 1)
print(min(answer, key=answer.get))