import sys
input = sys.stdin.readline

# 투포인터로 불가능한 경우를 찾는다.


def two_pointer(nums, start, end):
    # 중복이 없으면 end를 이ㅇ동
    # 중복이 있으면 st를 이동
    global count
    temp = set()
    temp.add(nums[end])
    while start <= end and end < n:
        print(start, end)
        if nums[end+1] in temp:
            temp.remove(nums[start])
            if start == end:
                start += 1
                end += 1
            else:
                start += 1
            count += end-start+1
        else:
            end += 1
            temp.add(nums[end])


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    two_pointer(nums, 0, 0)
    print(count)
