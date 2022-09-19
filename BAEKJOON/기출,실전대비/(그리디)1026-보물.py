n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
nums1.sort()
nums2.sort(reverse=True)
answer = 0
for i in range(n):
    answer += nums1[i]*nums2[i]
print(answer)
