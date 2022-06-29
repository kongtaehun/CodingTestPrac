def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return start


def countAB(A, B):
    count = 0
    for i in A:
        count += binarySearch(B, i, 0, len(B)-1)
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        A.sort()
        B = list(map(int, input().split()))
        B.sort()
        print(countAB(A, B))
