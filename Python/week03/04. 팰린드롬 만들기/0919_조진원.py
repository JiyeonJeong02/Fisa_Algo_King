name = input()

# 알파벳 개수 세기
name_count = dict()
for i in name :
    if i not in name_count :
        name_count[i] = 1
    else :
        name_count[i] += 1

# 알파벳 순 정렬
name_count = dict(sorted(name_count.items(), key = lambda x : x[0]))


answer = ''
# 조건확인
if len(name) % 2 == 0 :
    for char in name_count :
        if name_count[char] % 2 != 0 :
            answer = "I'm Sorry Hansoo"
            break
        answer += char * (name_count[char] // 2)
    if answer != "I'm Sorry Hansoo" :
        answer = answer + ''.join(reversed((answer)))
else :
    odds = 0
    for char in name_count :
        if name_count[char] % 2 != 0 :
            odd = char
            odds += 1
            if odds > 1 :
                answer = "I'm Sorry Hansoo"
                break

        answer += char * (name_count[char] // 2)
    if answer != "I'm Sorry Hansoo" :
        answer = answer + odd + ''.join(reversed((answer)))


print(answer)