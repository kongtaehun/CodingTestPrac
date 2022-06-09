def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            temp = yellow//i
            if i*2+temp*2+4 == brown:
                answer = [i+2, temp+2]
                answer.sort(reverse=True)
                return answer

    answer = []
    return answer
