n = 3; computers = 	[[1, 1, 0], [1, 1, 1], [0, 1, 1]];
from collections import deque
def solution(n, computers):
    connected = [False for i in range(n)]
    ans = 0
    for i in range(n):
        if not connected[i]:
            ans += 1
            connected[i] = True
            q = deque([i])
            while q:
                a = q.pop()
                for b in range(n):
                    if not connected[b] and computers[a][b] == 1:
                        connected[b] = True
                        q.append(b)
    return ans