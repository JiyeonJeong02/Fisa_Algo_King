#아이디 규칙에 맞지 않는 아이디 -> 입력된 아이디와 유사하면서 규칙에 맞는 아이디 추천

#규칙
#1. 3자 이상, 15자 이하
#소문자, 숫자, - ,_,.
#.는 처음과 끝 x, 연속x


import re

def solution(new_id):
    new_id = new_id.lower() #1단계
    new_id = re.sub('[^a-z0-9-_.]', '', new_id) #2단계
    new_id = re.sub('[.]+', '.', new_id) #3단계
    new_id = re.sub('^[.]|[.]$', '', new_id)# 4단계
    new_id = 'a' if new_id == '' else new_id #5단계
    new_id = new_id[:15] if len(new_id) > 15 else new_id #6단계
    new_id = re.sub('^[.]|[.]$', '', new_id)# 6-1단계
    
    if len(new_id) < 3: #7단계
        last = new_id[-1]
        while len(new_id) < 3:
            new_id += last
    
    

    return new_id