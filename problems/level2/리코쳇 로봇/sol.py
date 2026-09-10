board = [".D.R", "....", ".G..", "...D"]

N = len(board)
M = len(board[0])
start_y, start_x = 0, 0
end_y, end_x = 0, 0
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            start_y, start_x = i, j
        if board[i][j] == "G":
            end_y, end_x = i, j

start = next((r, c) for r in range(N) for c in range(M) if board[r][c] == "R")
goal = next((r, c) for r in range(N) for c in range(M) if board[r][c] == "D")

def slide(r, c, dr, dc):
    while 0 <= r + dr < N and 0 <= c + dc < M and board[r+dr][c+dc] != "D":
        r, c = r + dr, c + dc
    return r, c

dist = {start: 0}
q = deque([start])

def stops(y, x):
    left, right, top, bottom = [y, x], [y, x], [y, x], [y, x]
    while 0 < left[1] and board[left[0]][left[1]-1] != "D":
        left[1] -= 1

    while right[1] < M-1 and board[right[0]][right[1]+1] != "D":
        right[1] += 1

    while 0 < top[0]  and board[top[0]-1][top[1]] != "D":
        top[0] -= 1

    while bottom[0] < N-1 and board[bottom[0]+1][bottom[1]] != "D":
        bottom[0] += 1

    return (left, right, top, bottom)


from collections import deque
ans = -1
q = deque([(start_y, start_x, 0)])
while q:
    pos_y, pos_x, n = q.popleft()
    if (pos_y, pos_x) == (end_y, end_x):
        ans = n
        break

    visited[pos_y][pos_x] = True
    for stop_y, stop_x in stops(pos_y, pos_x):
        if visited[stop_y][stop_x]:
            continue
        q.append((stop_y, stop_x, n + 1))

    

print(ans)


from collections import deque
def solution(board):
    N = len(board)
    M = len(board[0])
    start_y, start_x = 0, 0
    end_y, end_x = 0, 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                start_y, start_x = i, j
            if board[i][j] == "G":
                end_y, end_x = i, j

    def stops(y, x):
        left, right, top, bottom = [y, x], [y, x], [y, x], [y, x]
        while 0 < left[1] and board[left[0]][left[1]-1] != "D":
            left[1] -= 1

        while right[1] < M-1 and board[right[0]][right[1]+1] != "D":
            right[1] += 1

        while 0 < top[0]  and board[top[0]-1][top[1]] != "D":
            top[0] -= 1

        while bottom[0] < N-1 and board[bottom[0]+1][bottom[1]] != "D":
            bottom[0] += 1

        return (left, right, top, bottom)



    ans = -1
    q = deque([(start_y, start_x, 0)])
    while q:
        pos_y, pos_x, n = q.popleft()
        if (pos_y, pos_x) == (end_y, end_x):
            ans = n
            break

        visited[pos_y][pos_x] = True
        for stop_y, stop_x in stops(pos_y, pos_x):
            if visited[stop_y][stop_x]:
                continue
            q.append((stop_y, stop_x, n + 1))

            

    return ans



