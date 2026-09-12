info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

from collections import defaultdict, deque
adj = defaultdict(list)
for a, b in edges:
    adj[a].append(b)

ans = -1
q = deque([({0}, 0, 0)])
while q:
    candi, sheep, score = q.popleft()
    for nxt in candi:
        nsheep = sheep + (1 if info[nxt] == 0 else 0)
        nscore = score + (1 if info[nxt] == 0 else -1)
        if nscore > 0:
            ncandi = set(v for v in candi if v != nxt)
            ncandi.update(adj[nxt])
            q.append((ncandi, nsheep, nscore))
            ans = max(nsheep, ans)

print(ans)

from collections import defaultdict, deque
def solution(info, edges):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)

    ans = -1
    q = deque([({0}, 0, 0)])
    while q:
        candi, sheep, score = q.popleft()
        for nxt in candi:
            nsheep = sheep + (1 if info[nxt] == 0 else 0)
            nscore = score + (1 if info[nxt] == 0 else -1)
            if nscore > 0:
                ncandi = set(v for v in candi if v != nxt)
                ncandi.update(adj[nxt])
                q.append((ncandi, nsheep, nscore))
                ans = max(nsheep, ans)

    return ans


            
