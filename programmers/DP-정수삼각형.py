def solution(triangle):
    triangle.reverse()
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] = max(triangle[i][j]+triangle[i-1]
                                 [j], triangle[i][j]+triangle[i-1][j+1])

    return triangle[len(triangle)-1][0]
