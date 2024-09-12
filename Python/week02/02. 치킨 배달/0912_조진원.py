N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

house = []
store = []

for x in range(N) :
    for y in range(N) :
        if city[x][y] == 1 :
            house.append((x,y))
        elif city[x][y] == 2 :
            store.append((x,y))
        else :
            pass

from itertools import combinations

answer = float('inf')
for case in combinations(store, M) :
    distance = 0
    for (x1,y1) in house :
        result = float('inf')
        for (x2,y2) in case :
            result = min(result, (abs(x2-x1) + abs(y2-y1)))
        distance += result    
    answer = min(answer, distance)

print(answer)