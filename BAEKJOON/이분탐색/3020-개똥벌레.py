import sys
input = sys.stdin.readline
# 이분탐색 0~7
# 최솟값을 찾는다.
# 그러한 최솟값을 갖는 구간을


# binary search로 얼마나 장애물 부수는 수를 구한다.
def getHowManyCrush(h, bottom_heights, top_heights, total_h):
    # 이진탐색1
    # - h가 몇번부딛히는지!
    # 높이가 h-0.5에 근접하는 인덱스가 나옴
    # h-0.5가 목표, 인덱스 0부터 h-1을 처음끝ㅇ으로 검색시작
    bottom_temp = len(bottom_heights) - binarySearch(bottom_heights,
                                                     h-0.5, 0, len(bottom_heights)-1)
    top_temp = len(top_heights) - binarySearch(top_heights,
                                               total_h-(h-0.5), 0, len(top_heights)-1)
    return bottom_temp+top_temp


def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return start


if __name__ == '__main__':

    n, h = map(int, input().split())
    botton_heights = []
    top_heights = []
    for i in range(n):
        if i % 2 == 0:
            botton_heights.append(int(input()))
        else:
            top_heights.append(int(input()))
    top_heights.sort()
    botton_heights.sort()

    min_crash = int(1e9)
    min_count = 0
    for i in range(1, h+1):
        crashCount = getHowManyCrush(i, botton_heights, top_heights, h)
        if min_crash > crashCount:
            min_crash = crashCount
            min_count = 1
        elif min_crash == crashCount:
            min_count += 1
    print(min_crash, min_count)
