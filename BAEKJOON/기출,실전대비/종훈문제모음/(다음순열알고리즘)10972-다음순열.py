
# peak-1과 그 큰값을 바꾼다.
# peak-1뒤로 오름차순 정렬한다.


# 마지막 오름차순이 끝나는 지점(peak) -1 를 찾는다.
def getPeak(nums):
    for i in range(n-1, 0, -1):
        if nums[i] > nums[i-1]:
            return i
    return -1
# 뒤에서 부터 peak-1보다 큰값(idx)을 찾는다.


def getMaxThanPeak(nums, peak):
    for i in range(n-1, 0, -1):
        if nums[i] > nums[peak-1]:
            return i
    return -1


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    peak = getPeak(nums)
    if peak == -1:
        print(-1)
        exit(0)
    max_idx = getMaxThanPeak(nums, peak)
    if max_idx != -1:
        nums[max_idx], nums[peak-1] = nums[peak-1], nums[max_idx]

    nums = nums[:peak] + sorted(nums[peak:])
    print(' '.join(list(map(str, nums))))
