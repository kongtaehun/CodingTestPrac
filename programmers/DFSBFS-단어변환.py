def dfs(visited, start, graph, count):
    visited[start] = count
    for i in graph[start]:
        if visited[i] >= count or visited[i] == 0:
            dfs(visited, i, graph, count+1)


def linkCheck(a, b):
    n = len(a)
    a = list(a)
    b = list(b)
    check = 0
    for i in range(n):
        if a[i] != b[i]:
            check += 1
    if check == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    # 변환하지 못하는 경우 예외-------
    if target not in words:
        return 0
    # --------------------------

    # 단어 합치기
    all_words = [begin]
    for i in words:
        all_words.append(i)
    all_words.append(target)

    # 그래프 초기화 : begin부터 한글자로 바꿀수 있는 것들을 연결한다.
    graph = [[] for i in range(len(all_words))]
    for first in range(len(all_words)):
        for second in range(len(all_words)):
            if first != second:
                if linkCheck(all_words[first], all_words[second]):
                    graph[first].append(second)
    visited = [0 for i in range(len(all_words))]

    dfs(visited, 0, graph, 0)

    return visited[-1]
