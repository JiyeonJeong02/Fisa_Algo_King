#비밀지도

def solution(n, arr1, arr2):
    arr1_bin = [str(bin(i))[2:].zfill(n) for i in arr1] #이진수 변환
    arr2_bin = [str(bin(i))[2:].zfill(n) for i in arr2]

    answer = []

    for a, b in zip(arr1_bin, arr2_bin):
        ans_str = ''
        for i in range(n):
            if a[i] == '0' and b[i] == '0' :
                ans_str += ' '
            else:
                ans_str += '#'
        answer.append(ans_str)

    return answer
