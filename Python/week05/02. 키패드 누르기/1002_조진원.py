# 빡구현

def solution(numbers, hand):
    answer = ''
    
    left = [3,0]
    right = [3,2]
    
    for number in numbers :
        
        if number == 1 :
            answer += 'L'
            left = [0,0]
        elif number == 4 :
            answer += 'L'
            left = [1,0]
        elif number == 7 :
            answer += 'L'
            left = [2,0]
            
        elif number == 3 :
            answer += 'R'
            right = [0,2]
        elif number == 6 :
            answer += 'R'
            right = [1,2]
        elif number == 9 :
            answer += 'R'
            right = [2,2]
            
        elif number == 2 :
            loc = [0,1]
            l_dt = sum(abs(left[i] - loc[i]) for i in range(2))
            r_dt = sum(abs(right[i] - loc[i]) for i in range(2))
            
            if l_dt < r_dt :
                answer += 'L'
                left = loc
            elif l_dt > r_dt :
                answer += 'R'
                right = loc
            else :
                if hand == 'left' :
                    answer += 'L'
                    left = loc
                else :
                    answer += 'R'
                    right = loc

        elif number == 5 :
            loc = [1,1]
            l_dt = sum(abs(left[i] - loc[i]) for i in range(2))
            r_dt = sum(abs(right[i] - loc[i]) for i in range(2))
            
            if l_dt < r_dt :
                answer += 'L'
                left = loc
            elif l_dt > r_dt :
                answer += 'R'
                right = loc
            else :
                if hand == 'left' :
                    answer += 'L'
                    left = loc
                else :
                    answer += 'R'
                    right = loc

        elif number == 8 :
            loc = [2,1]
            l_dt = sum(abs(left[i] - loc[i]) for i in range(2))
            r_dt = sum(abs(right[i] - loc[i]) for i in range(2))
            
            if l_dt < r_dt :
                answer += 'L'
                left = loc
            elif l_dt > r_dt :
                answer += 'R'
                right = loc
            else :
                if hand == 'left' :
                    answer += 'L'
                    left = loc
                else :
                    answer += 'R'
                    right = loc
                    
        elif number == 0 :
            loc = [3,1]
            l_dt = sum(abs(left[i] - loc[i]) for i in range(2))
            r_dt = sum(abs(right[i] - loc[i]) for i in range(2))
            
            if l_dt < r_dt :
                answer += 'L'
                left = loc
            elif l_dt > r_dt :
                answer += 'R'
                right = loc
            else :
                if hand == 'left' :
                    answer += 'L'
                    left = loc
                else :
                    answer += 'R'
                    right = loc
    return answer