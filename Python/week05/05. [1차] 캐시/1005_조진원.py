def solution(cacheSize, cities):
    answer = 0
    
    # 0 이면 그냥 5를 곱한다.
    if cacheSize == 0 :
        return len(cities) * 5
    
    else :
        cash = dict()
        for i, city in enumerate(cities) :
            # 소문자로 변환
            city = city.lower()
            
            # 캐시 히트
            if city in cash :
                answer += 1
                cash[city] = i
            else :
                # 캐시 미스
                if len(cash) < cacheSize:
                    answer += 5
                    cash[city] = i
                else :
                    answer += 5
                    out_cash = min(cash, key = cash.get)
                    del cash[out_cash]
                    cash[city] = i
                    
        return answer