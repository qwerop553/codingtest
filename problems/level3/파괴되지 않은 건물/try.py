def solution(board, skill):

    N = len(board)
    M = len(board[0])
    paper = [[0] * (M+1) for _ in range(N+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        paper[r1][c1] += (degree if type==2 else -degree)
        paper[r1][c2+1] -= (degree if type==2 else -degree)
        paper[r2+1][c1] -= (degree if type==2 else -degree)
        paper[r2+1][c2+1] += (degree if type==2 else -degree)
        
    for x in range(M+1):
        for y in range(1, N+1):
            paper[y][x] += paper[y-1][x]
            
    for y in range(N+1):
        for x in range(1, M+1):
            paper[y][x] += paper[y][x-1]
            
    ans = 0
    for y in range(N):
        for x in range(M):
            if board[y][x]+paper[y][x] > 0: ans += 1
        
    
            
    return ans
