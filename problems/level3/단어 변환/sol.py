def dist(a, b):
    return sum(1 for i in range(len(a)) if a[i] != b[i])


begin = 'hit'; target = 'cog' ; words = ["hot", "dot", "dog", "lot", "log"]
words = [begin] + words + [target]

adj = [[] for i in range(len(words))]
visited = [0] + [float('inf') for _ in range(len(words)-1)]
takes = [0] * len(words)
for i in range(len(words)):
    for j in range(i, len(words)):
        if dist(words[i], words[j]) == 1:
            adj[i].append(j)
            adj[j].append(i)
from collections import deque
q = deque([0])
while q:
    cur = q.popleft()
    for v in adj[cur]:
        if visited[cur] + 1 < visited[v]:
            visited[v] = visited[cur] + 1
            q.appendleft(v)

print(visited) 

from collections import deque
def dist(a, b):
    return sum(1 for i in range(len(a)) if a[i] != b[i])

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words = [begin] + words + [target]
    
    adj = [[] for i in range(len(words))]
    for i in range(len(words)):
        for j in range(i, len(words)):
            if dist(words[i], words[j]) == 1:
                adj[i].append(j)
                adj[j].append(i)

    visited = [0] + [float('inf') for _ in range(len(words)-1)]


    q = deque([0])
    while q:
        cur = q.popleft()
        for v in adj[cur]:
            if visited[cur] + 1 < visited[v]:
                visited[v] = visited[cur] + 1
                q.appendleft(v)

    return visited[-1]