# 최대값 밑으로 내려갈수 없다는 예외를 생각하지 못함

def getNeededCountOfBluRay(maxSizeOfBluRay, videos):
    count = 1
    sizeOfOneBluRay = 0
    for i in range(len(videos)):
        sizeOfOneBluRay += videos[i]
        if sizeOfOneBluRay > maxSizeOfBluRay:
            count += 1
            sizeOfOneBluRay = videos[i]
            i -= 1

    return count


def binarySearch(videos, target):
    start = 0
    end = len(videos)*max(videos)
    while start <= end:
        mid = (start+end)//2
        bluRayCount = getNeededCountOfBluRay(mid, videos)

        if bluRayCount > target:
            start = mid+1
        else:
            end = mid-1
    return start


if __name__ == '__main__':
    n, m = map(int, input().split())
    videos = list(map(int, input().split()))
    result = binarySearch(videos, m)
    print(max(videos) if result < max(videos) else result)
