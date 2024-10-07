from collections import deque

def solution(cacheSize, cities):
    
    answer = 0
    cpu = deque()
    
    for city in cities:
        city = city.lower()
        if (len(cpu) < cacheSize) and (city not in cpu):
            cpu.append(city)
            answer += 5
        else:
            if city not in cpu:
                cpu.append(city)
                answer += 5
                cpu.popleft()
            else:
                answer += 1
                cpu.remove(city)
                cpu.append(city)
    return answer