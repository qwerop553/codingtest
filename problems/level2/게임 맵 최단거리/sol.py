maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

N, M = len(maps), len(maps[0])

start = (0, 0)
goal = (N-1, M-1)

dist = {start: 1}

from collections import deque
q = deque([start])

while q:
    r, c = q.popleft()
    if (r, c) == goal: break
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        next_r, next_c = r + dr, c + dc
        if 0 <= next_r < N and 0 <= next_c < M and maps[next_r][next_c] != 0 and (next_r, next_c) not in dist:
            dist[(next_r, next_c)] = dist[(r, c)] + 1
            q.append((next_r, next_c))

print(dist.get(goal, -1))
            
from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    start, goal = (0, 0), (N-1, M-1)
    dist = {start: 1}

    q = deque([start])

    while q:
        r, c = q.popleft()
        if (r, c) == goal: break
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_r, next_c = r + dr, c + dc
            # if 조건이 너무 길면 나눠서 continue 문을 사용해!
            if 0 <= next_r < N and 0 <= next_c < M and maps[next_r][next_c] != 0 and (next_r, next_c) not in dist:
                dist[(next_r, next_c)] = dist[(r, c)] + 1
                q.append((next_r, next_c))