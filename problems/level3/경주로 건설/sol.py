board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]


import heapq
def solution(board):
    N = len(board)
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

    def can_walk(y, x):
        if not (0 <= y < N and 0 <= x < N):
            return False
        if board[y][x] == 1:
            return False
        return True
    
    q = [(0, 0, 0, -1)]

    while q:
        expense, y, x, direction = heapq.heappop(q)
        if (y, x) ==(N-1, N-1):
            return expense
        
        for dir, dy, dx in ((UP, -1, 0), (DOWN, 1, 0), (LEFT, 0, -1), (RIGHT, 0, 1)):
            if can_walk(y+dy, x+dx):
                if dir == direction:
                    heapq.heappush(q, (expense+100, y+dy, x+dx, dir))
                else:
                    heapq.heappush(q, (expense+600, y+dy, x+dx, dir))


print(solution(board))

