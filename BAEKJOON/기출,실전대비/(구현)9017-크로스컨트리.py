from collections import Counter

for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    # count,1~4vsum, 5~6list
    scores = [[0, 0, i, []] for i in range(max(nums)+1)]
    fail_team = set()
    count = dict(Counter(nums))
    for i in count.keys():
        if count[i] != 6:
            fail_team.add(i)

    score = 1
    for i in range(n):
        if nums[i] not in fail_team:
            scores[nums[i]][0] += 1
            scores[nums[i]][2] = nums[i]
            if scores[nums[i]][0] <= 4:
                scores[nums[i]][1] += score
                score += 1
            else:
                scores[nums[i]][3].append(score)
                score += 1

    scores.sort(key=lambda x: (x[1], x[3]))

    for i in range(1, len(scores)):
        if scores[i][0] == 6:
            print(scores[i][2])
            break
