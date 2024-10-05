def solution(survey, choices):
    num1 = dict({'R' : 0, 'T' : 0})
    num2 = dict({'C' : 0, 'F' : 0})
    num3 = dict({'J' : 0, 'M' : 0})
    num4 = dict({'A' : 0, 'N' : 0})
    
    for a, b in zip(survey, choices) :
        if a in ['RT', 'TR'] :
            if b > 4 :
                num1[a[1]] += (b-4)
            elif b < 4 :
                num1[a[0]] += (4-b)
        
        elif a in ['FC','CF'] :
            if b > 4 :
                num2[a[1]] += (b-4)
            elif b < 4 :
                num2[a[0]] += (4-b)
                
        elif a in ['MJ','JM'] :
            if b > 4 :
                num3[a[1]] += (b-4)
            elif b < 4 :
                num3[a[0]] += (4-b)
            
        elif a in ['AN','NA'] :
            if b > 4 :
                num4[a[1]] += (b-4)
            elif b < 4 :
                num4[a[0]] += (4-b)
    
    answer = ''
    answer += sorted(num1.items(), key = lambda x : (-x[1],x[0]))[0][0]
    answer += sorted(num2.items(), key = lambda x : (-x[1],x[0]))[0][0]
    answer += sorted(num3.items(), key = lambda x : (-x[1],x[0]))[0][0]
    answer += sorted(num4.items(), key = lambda x : (-x[1],x[0]))[0][0]
    return answer