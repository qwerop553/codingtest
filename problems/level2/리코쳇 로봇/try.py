"""
DFS로 풀거야
DFS도 방문한 곳을 체크하는 것은 필요해
그러나 Dict형태로 저장할 수도 있어.
Dict형태로 처리하자.

어느 방향으로 갈 수 있는지를 확인하는 과정이 까다롭지.
slide 함수로 해당 방향으로 특정 방향으로 이동하려고 할 때, 멈춰지는 좌표를 리턴하자.

시작점, 끝 점의 위치 저장
시작점을 적음
deque로 왼쪽, 오른쪽, 우측, 아래 탐색. +1 한 값 저장. 이미 key가 있다면 해당 값 저장하지 않고 큐에도 넣지 않음.
"""

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]


def slide(r, c):
    ret = []
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r, c
        while 0 <= nr + dr < N and 0 <= nc + dc < M and board[nr+dr][nc+dc] != "D":
            nr, nc = nr + dr, nc + dc
        ret.append((nr, nc))
    return ret 

from collections import deque
def solution(board):
    N = len(board)
    M = len(board[0])
    R = next((r, c) for r in range(N) for c in range(M) if board[r][c] == "R")
    G = next((r, c) for r in range(N) for c in range(M) if board[r][c] == "G")
    dist = {R:0}

    def slide(r, c):
        ret = []
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r, c
            while 0 <= nr + dr < N and 0 <= nc + dc < M and board[nr+dr][nc+dc] != "D":
                nr, nc = nr + dr, nc + dc
            ret.append((nr, nc))
        return ret 

    q = deque([R])
    while q:
        cur = q.popleft()
        if cur == G:
            return dist[G]
        for nxt in slide(*cur):
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    return -1

    





