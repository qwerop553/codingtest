from collections import deque


def solution(maps):
    H, W = len(maps), len(maps[0])
    visited = [[False] * W for _ in range(H)]

    def bfs(start_y, start_x):
        """시작 칸이 속한 섬의 식량 합을 반환한다."""
        visited[start_y][start_x] = True
        total = int(maps[start_y][start_x])
        q = deque([(start_y, start_x)])

        while q:
            y, x = q.popleft()
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < H and 0 <= nx < W):
                    continue
                if visited[ny][nx] or maps[ny][nx] == "X":
                    continue
                visited[ny][nx] = True
                total += int(maps[ny][nx])
                q.append((ny, nx))

        return total

    answer = []
    for y in range(H):
        for x in range(W):
            if not visited[y][x] and maps[y][x] != "X":
                answer.append(bfs(y, x))

    return sorted(answer) if answer else [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))  # [1, 3, 16]