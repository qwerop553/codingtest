'''
트리

항상  set에 트리의 구성 요소를 넣고, 단 한 번! 순환한다고 해서 
모두 채워지지 않는 것에 유의하시오. 간접적으로 연결될 수 있음.
그래서 부울대수로 행렬곱 하자네
'''
n = 7; wires = 	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

from collections import deque
def solution(n, wires):
    ans = []
    for i in range(n):
        adj = [ [] for _ in range(n+1)]
        for j, (a, b) in enumerate(wires):
            if j == i: continue
            adj[a].append(b)
            adj[b].append(a)

        visited = set([1])
        q = deque([1])
        while q:
            s = q.popleft()
            for v in adj[s]:
                if v not in visited:
                    q.appendleft(v)
                    visited.add(v)

        ans.append(abs(n-2*len(visited)))

    return min(ans)

