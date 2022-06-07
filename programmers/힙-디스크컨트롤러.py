import heapq


def solution(jobs):
    # jobs 정렬
    end_len = len(jobs)
    # 현재 쌓인 요청들
    requests = []
    jobs.sort(key=lambda x: (x[0]))
    대기시간 = []
    t = 0
    while True:
        if len(jobs) != 0:
            # 요청받기 (요청중에 현재시간보다 작은거 넣기)
            cnt = 0
            for job in jobs:
                if job[0] <= t:
                    heapq.heappush(requests, (job[1], job[0]))
                    cnt += 1
            for i in range(cnt):
                jobs.pop(0)

        if requests:
            now = heapq.heappop(requests)
            대기시간.append(t+now[0]-now[1])
            t = t+now[0]
        else:
            t += 1

        # 끝내기
        if len(대기시간) == end_len:
            break

    return int(sum(대기시간)/len(대기시간))
