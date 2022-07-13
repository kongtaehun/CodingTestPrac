# 값의 범위에 유의 하자!!!!!!
# INF는 문제에 따라 달라질 수 있다.
INF = int(1e10)


def search_two_pointer(arr):
    global result, answer

    l = 0
    r = len(arr)-1
    while l < r:
        temp = arr[l]+arr[r]
        if abs(temp) <= result:
            result = abs(temp)
            answer = [l, r]

        if temp < 0:
            l += 1
        else:
            r -= 1
    return answer


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    result = INF
    answer = [0, len(nums)-1]
    search_two_pointer(nums)

    print(nums[answer[0]], nums[answer[1]])
