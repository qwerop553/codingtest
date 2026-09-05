n = 5



def solution(n):
    tri = [[-1] * (i + 1) for i in range(n)]
    r, c = -1, 0
    moves = ((1, 0), (0, 1), (-1, -1))
    dr, dc = moves[0]
    j = 0
    cur = 1

    def valid(r, c) -> bool:
        return 0<= c <= r < n and tri[r][c] == -1

    while True:
        next_r, next_c = r+dr, c+dc
        if valid(next_r, next_c):
            tri[next_r][next_c] = cur
            r, c = next_r, next_c
            cur += 1

        else:
            fail = 0
            while not valid(r+dr, c+dc):
                j += 1
                dr, dc = moves[j%3]
                fail += 1
                if fail == 3: break
            if fail == 3: break

    ans = []
    for row in tri:
        for x in row:
            ans.append(x)

    return ans 
        