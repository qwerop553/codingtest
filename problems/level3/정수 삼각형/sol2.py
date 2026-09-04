triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
def solution(triangle):
    prev = [0, triangle[0][0], 0]
    for i, line in enumerate(triangle[1:], start=2):
        cur = [0] * (i + 2)
        for j, num in enumerate(line, start=1):  
            cur[j] = max(prev[j-1], prev[j]) + num
        prev = cur
    return max(prev)