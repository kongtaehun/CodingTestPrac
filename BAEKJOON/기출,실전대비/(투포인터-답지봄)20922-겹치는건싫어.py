# 특정조건을 만족하는 부분수열 구하기
# 앞에서부터 두개의 투포인터가 끝까지 검사하면서 최댓값을 저장
import sys


def two_pointer(arr):
    global answer
    l = 0
    r = 0
    while r < n:
        print(arr[l:r+1])
        if dp[arr[r]] < k:
            dp[arr[r]] += 1
            r += 1
        else:
            dp[arr[l]] -= 1
            l += 1
        answer = max(answer, r-l)
    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0]*(100001)
    answer = 0
    if len(arr) == 1:
        print(1)
    else:
        print(two_pointer(arr))
