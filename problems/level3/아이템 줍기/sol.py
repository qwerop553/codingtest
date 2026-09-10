rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8

from collections import deque
N = 50
M = 50
def slide(r, c, dr, dc):
    if all([
        0 <= r + dr < N,
        0 <= c + dc < M,
        all(not inside(rect, r + dr, c + dc) for rect in rectangle),
        any(border(rect, r + dr/2, c + dc/2) for rect in rectangle)
    ]): return True
    return False

def inside(rect, r, c):
    return (rect[0] < r < rect[2] and rect[1] < c < rect[3])

def border(rect, r, c):
    return (rect[0] <= r <= rect[2] and (rect[1] == c or rect[3] == c)) or (rect[1] <= c <= rect[3] and (rect[0] == r or rect[2] == r))


start = (characterX, characterY)
goal = (itemX, itemY)
dist = {start: 0}
q = deque([start])


from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 51
    M = 51
    def slide(r, c, dr, dc):
        if all(not inside(rect, r + dr, c + dc) for rect in rectangle) and any(border(rect, r + dr/2, c + dc/2) for rect in rectangle): 
            return True
        return False

    def inside(rect, r, c):
        return (rect[0] < r < rect[2] and rect[1] < c < rect[3])

    def border(rect, r, c):
        return (rect[0] <= r <= rect[2] and (rect[1] == c or rect[3] == c)) or (rect[1] <= c <= rect[3] and (rect[0] == r or rect[2] == r))


    start = (characterX, characterY)
    goal = (itemX, itemY)
    dist = {start: 0}
    q = deque([start])

    while q:
        r, c = q.popleft()
        if (r, c) == (itemX, itemY):
            return dist[goal]
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if slide(r, c, dr, dc) and (r+dr, c+dc) not in dist:
                dist[(r+dr, c+dc)] = dist[(r, c)] + 1
                q.append((r+dr, c+dc))

    return -1

        