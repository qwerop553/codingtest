maps = ["X591X","X1X5X","X231X", "1XXX1"]

from collections import deque
def solution(maps):
    H = len(maps)
    W = len(maps[0])
    visited = [[False] * W for _ in range(H)]
    islands = []

    def bfs(y, x):
        total = int(maps[y][x])
        visited[y][x] = True
        q = deque([(y, x)])
        while q:
            b, a = q.popleft()
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                v, u = b + dy, a + dx
                if not (0 <= v < H and 0 <= u < W):
                    continue
                if maps[v][u] == 'X' or visited[v][u]:
                    continue
                            
                total += int(maps[v][u])
                visited[v][u] = True
                q.append((v, u))

        return total

    ans = []
    for y in range(H):
        for x in range(W):
            if maps[y][x] != 'X' and not visited[y][x]:
                ans.append(bfs(y, x))

    return sorted(ans) if ans else [-1]

print(solution(maps))

