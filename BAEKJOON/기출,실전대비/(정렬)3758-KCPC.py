

INF = int(1e9)
if __name__ == '__main__':
    for i in range(int(input())):
        n, k, IDt, m = map(int, input().split())
        submit_cnt = [0]*(n)
        submit_last = [INF]*(n)
        grades = [[0]*(k) for i in range(n)]
        for i in range(m):
            ID, prob_num, grade = map(int, input().split())
            team_idx = ID-1
            prob_idx = prob_num-1
            submit_last[team_idx] = i+1
            submit_cnt[team_idx] += 1
            grades[team_idx][prob_idx] = max(grade, grades[team_idx][prob_idx])

        result_list = [[] for i in range(n)]
        for i in range(n):
            result_list[i].append(i)
            result_list[i].append(sum(grades[i]))
            result_list[i].append(submit_cnt[i])
            result_list[i].append(submit_last[i])
        result_list.sort(key=lambda x: (-x[1], x[2], x[3]))
        # print(result_list)
        for i, v in enumerate(result_list):
            if v[0] == IDt-1:
                print(str(i+1))
                break
