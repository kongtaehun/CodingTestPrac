
import heapq
if __name__ == '__main__':
    k, n = map(int, input().split())
    nums = list(map(int, input().split()))
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    result = []
    cnt = 0
    result = set()
    while cnt < n:
        # 힙에서 최소값 꺼내기
        temp = heapq.heappop(heap)
        # 결과에서 중복된 결과가 있는지 확인
        if temp in result:
            continue
        # 없을 떄 실행과정
        result.add(temp)  # 결과배열에 꺼낸값 입력
        for i in range(k):  # 각값과 곱해서 다시 힙에 집어넣는다.
            heapq.heappush(heap, temp*nums[i])
        cnt += 1
    print(max(result))
    # print(heap)
