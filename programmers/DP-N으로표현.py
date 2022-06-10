def solution(N, number):
    answer = -1
    dp = [[] for i in range(10)]
    # N을 i만큼 사용하였을 때
    for i in range(1, 9):
        dp[i].append(int(str(N)*i))
        # i일 때 1~i-1까지
        for j in range(1, i):
            for front in dp[j]:
                for back in dp[i-j]:
                    dp[i].append(front+back)
                    dp[i].append(front-back)
                    dp[i].append(front*back)
                    if back != 0:
                        dp[i].append(front//back)
        # 중복제거
        dp[i] = list(set(dp[i]))

        # 검사하기
        if number in dp[i]:
            answer = i
            break

    return answer
