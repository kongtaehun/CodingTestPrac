

def dfs(x, start):
    global min_result
    if x == (n//2):
        difTeam = calAbility(team1)
        min_result = min(min_result, difTeam)

    else:
        for i in range(start, n+1):
            if visited[i] == 0:
                team1[x] = i
                visited[i] = 1
                dfs(x+1, i)
                visited[i] = 0
                team1[x] = 0


def calAbility(team1):
    team1_set = set(team1)
    team2_set = set()
    for i in range(1, n+1):
        if i not in team1_set:
            team2_set.add(i)
    team1_set = list(team1_set)
    team2_set = list(team2_set)
    team1_power = 0
    for i in range(n//2):
        for j in range(i, n//2):
            temp = board[team1_set[i]-1][team1_set[j]-1] + \
                board[team1_set[j]-1][team1_set[i]-1]
            team1_power += temp
    team2_power = 0
    for i in range(n//2):
        for j in range(i, n//2):
            temp = board[team2_set[i]-1][team2_set[j]-1] + \
                board[team2_set[j]-1][team2_set[i]-1]
            team2_power += temp

    return abs(team1_power-team2_power)


if __name__ == '__main__':
    n = int(input())
    visited = [0]*(n+1)
    min_result = int(1e9)
    board = []
    team1 = [0]*(n//2)
    for i in range(n):
        board.append(list(map(int, input().split())))

    dfs(0, 1)
    print(min_result)
