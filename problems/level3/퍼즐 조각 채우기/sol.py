game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]


def find(game_board, target):
    holes = []
    N, M = len(game_board), len(game_board[0])
    from collections import deque
    for i in range(N):
        for j in range(M):
            if game_board[i][j] == target:
                q = deque([(i, j)])
                game_board[i][j] = -1
                hole = []
                while q:
                    y, x = q.popleft()
                    hole.append((y, x))
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if not (0 <= ny < N and 0 <= nx < M): continue
                        if game_board[ny][nx] == target:
                            game_board[ny][nx] = -1
                            q.append((ny, nx))
                holes.append(hole)
    return holes

def normalize(block):
    min_r = min([r for r, _ in block])
    min_c = min([c for _, c in block])
    return sorted([(r - min_r, c - min_c) for r, c in block])

def rotate(block):
    return normalize([(-c, r) for r, c in block])

def solution(gmae_board, table):
    holes = [normalize(hole) for hole in find(game_board, 0)]
    blocks = [normalize(block) for block in find(table, 1)]
    used_block = [False] * len(blocks)
    used_hole = [False] * len(holes)

    ans = 0
    for i, hole in enumerate(holes):
        for j, block in enumerate(blocks):
            if used_hole[i]: break
            if used_block[j]: continue
            for _ in range(4):
                block = rotate(block)
                if block == hole:
                    ans += len(hole)
                    used_hole[i] = True
                    used_block[j] = True 
                    break # 회전을 멈춤

    return ans
        

print(ans)










