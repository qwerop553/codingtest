n = 6; edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]];
from collections import defaultdict, deque
def solution(n, edges):
    INF = float('inf')
    dp = [INF for i in range(n+1)]
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    q = deque([(1, 0)])
    while q:
        cur, cnt = q.pop()
        if dp[cur] < cnt: continue
        for nxt in adj[cur]:
            if cnt + 1 < dp[nxt]:
                dp[nxt] = cnt + 1
                q.append((nxt, cnt + 1))

    goal = dp[2:]
    return goal.count(max(goal))

