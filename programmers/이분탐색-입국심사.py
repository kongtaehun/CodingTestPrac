# 정답후보의 시간동안 심사관각각 몇명을 심사할 수 있는지
# 그 다음에 둘을 더한 값이 6이상일 때

# start가 end보다 커졌을 때 그만
def solution(n, times):
    start = 1
    end = max(times)*n
    while start <= end:

        mid = (start+end)//2
        count = 0
        for i in times:
            count += mid//i

        if count >= n:
            end = mid-1
        else:
            start = mid+1

    return start
