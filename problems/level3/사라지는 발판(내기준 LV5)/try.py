board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]


def solution(board, aloc, bloc):
    def dfs(turn, moves):
        nonlocal aloc, bloc
        movable = []
        if turn == "A":
            y, x = aloc
            if board[y][x] == 0:
                return ("B", moves)
            for a, b in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == 1:
                    aloc = [a, b]
                    board[y][x] = 0
                    movable.append(dfs("B", moves+1))
                    aloc = [y, x]
                    board[y][x] = 1
            if len(movable) == 0:
                return ("B", moves)
            return ("A", min(move[1] for move in movable if move[0]=="A")) if any(move[0]=="A" for move in movable) else ("B", max(move[1] for move in movable))
        else:
            y, x = bloc
            if board[y][x] == 0:
                return ("A", moves)
            for a, b in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == 1:
                    bloc = [a, b]
                    board[y][x] = 0
                    movable.append(dfs("A", moves+1))
                    bloc = [y, x]
                    board[y][x] = 1
            if len(movable) == 0:
                return ("A", moves)
            return ("B", min(move[1] for move in movable if move[0]=="B")) if any(move[0]=="B" for move in movable) else ("A", max(move[1] for move in movable))
        
    return dfs("A", 0)[1]



