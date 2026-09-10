import heapq

def solution(board):
    N = len(board)
    DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
    INF = float('inf')

    best = {}                    # (y, x, 방향) -> 그 상태 최소 비용
    q = [(0, 0, 0, -1)]          # (비용, y, x, 방향), -1 = 아직 방향 없음(출발점)

    while q:
        cost, y, x, d = heapq.heappop(q)
        if (y, x) == (N - 1, N - 1):
            return cost
        if best.get((y, x, d), INF) < cost:
            continue                              # 이미 더 싸게 온 적 있음 (넣었던 값이 쓸모 없어짐)
        for nd, (dy, dx) in enumerate(DIRS):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N) or board[ny][nx]:
                continue
            ncost = cost + (100 if nd == d or d == -1 else 600)
            if ncost < best.get((ny, nx, nd), INF): # 넣을 떄 확인함
                best[(ny, nx, nd)] = ncost  
                heapq.heappush(q, (ncost, ny, nx, nd))
    return -1