from collections import deque


n = 4

from collections import deque
def valid(ls):
    diag1 = []
    diag2 = []
    for y, x in enumerate(ls):
        diag1.append((y-x))
        diag2.append((2*n-x-y))
    if len(set(diag1)) != len(diag1) or len(set(diag2)) != len(diag2) or len(set(ls)) != len(ls):
        return False
    return True 

def solution(n):
    ans = 0 
    q = deque([[i] for i in range(n)])
    while q:
        qpos = q.popleft()
        if len(qpos) == n:
            ans += 1
            continue

        for i in range(n):
            if valid(qpos + [i]):
                q.append(qpos + [i])

    return ans