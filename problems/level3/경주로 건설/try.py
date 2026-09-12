"""
기존에 BFS로 접근했을 때 예제 14가 오답이었음.
그것은, visited가 list고, 모든 BFS가 같은 list를 공유하게 되어,
결국 Greedy한 해법이었기 때문이었다.

따라서 이 문제는 Dijkstra DP로 접근해야 정확한 해결책이되,
위치와 더불어 어떤 방향으로 접근했는지를 기억할 필요가 있다.
즉 특정 위치에 특정 방향으로 접근하는 최소 금액을 저장한다. 그런데..
특정 구간에 도달만 하면.. 가장 저렴한가?
특정 지점에 특정 방향으로 오는 것이 무언가 희생할 여지는 없나?
여기서는 없지만, 다른 문제도 있을 수가 있네... 
예를 들어 편도가 아닌 왕복인 경우, (돌아가는 금액이 더 비싸다면)
이 방법도 틀릴 수가 있겠다.

힙을 사용한다.

한 칸씩 가면 되니까 valid 정도면 충분한 것 같다."""


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


import heapq
def solution(board):
    INF = float('inf')
    N = len(board)
    DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)] # Left, right, up, down
    best = {}
   
    def valid(r, c):
        return (0 <= r < N and 0 <= c < N) and board[r][c] == 0
            

    q = []
    heapq.heappush(q, (0, 0, 0, 1))
    heapq.heappush(q, (0, 0, 0, 3))

    while q:
        cost, r, c, d = heapq.heappop(q)
        if (r, c) == (N-1, N-1):
            return cost
        if cost > best.get((r, c, d), INF): continue
        for nd, (dr, dc) in enumerate(DIR):
            if not valid(r+dr, c+dc): continue
            ncost = cost + (100 if nd == d else 600)
            if best.get((r+dr, c+dc, nd), INF) < ncost: continue
            best[(r+dr, c+dc, nd)] = ncost
            heapq.heappush(q, (ncost, r+dr, c+dc, nd))
            
    return -1

print(solution(board))


