# 다음 순열 알고리즘
# 1. 순열의 마지막 peak(peak뒤로는 오름차순이 없을때) 인덱스를 찾는다.(peak)
# 2. peak-1을 기준으로 뒤에서부터 peak-1보다 첫번째 큰값을 교환한다.
# 3. peak을 오름차순으로 정렬하고 순열[:peak]을 합친다.
def prev_permutation(n, nums):
    # 1번 과정
    peak_idx = -1  # peak이 -1이면 마지막 순열이라는 뜻
    for i in range(n-1, 0, -1):
        if nums[i] < nums[i-1]:
            peak_idx = i
            break
    if peak_idx == -1:
        return -1
    # 2번 과정
    for i in range(n-1, 0, -1):
        if nums[peak_idx-1] > nums[i]:
            nums[peak_idx-1], nums[i] = nums[i], nums[peak_idx-1]
            break
    # 3번과정
    nums = nums[:peak_idx]+sorted(nums[peak_idx:], reverse=True)
    return ' '.join(list(map(str, nums)))


n = int(input())
nums = list(map(int, input().split()))
print(prev_permutation(n, nums))
