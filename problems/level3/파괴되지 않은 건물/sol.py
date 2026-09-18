def solution(board, skill):
    n, m = len(board), len(board[0])
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    for t, r1, c1, r2, c2, degree in skill:
        d = -degree if t == 1 else degree
        diff[r1][c1] += d
        diff[r1][c2 + 1] -= d
        diff[r2 + 1][c1] -= d
        diff[r2 + 1][c2 + 1] += d

    # 가로 누적
    for row in diff:
        acc = 0
        for x in range(m + 1):
            acc += row[x]
            row[x] = acc

    # 세로 누적 + 정답 카운트 동시에
    ans = 0
    for y in range(n):
        if y > 0:
            row, above = diff[y], diff[y - 1]
            for x in range(m):
                row[x] += above[x]
        row, b = diff[y], board[y]
        for x in range(m):
            if b[x] + row[x] > 0:
                ans += 1

    return ans