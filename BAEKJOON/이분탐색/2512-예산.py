# 0. 정렬
# 1. 최적값에 수렴해야함
# 2. 기준 : 상한가
#       최소 - 1
#       최대 - 예산요청 최댓값

def getAllBudget(nums, mid):
    result = 0
    for i in nums:
        if i-mid <= 0:
            result += i
        else:
            result += mid
    return result


def binary_search(nums, target):
    start = 1
    end = max(nums)
    while start <= end:
        mid = (start+end)//2
        budget = getAllBudget(nums, mid)
        if target < budget:
            end = mid-1
        else:
            start = mid+1
    return start


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    total = int(input())
    result = binary_search(nums, total)
    print(result-1)
