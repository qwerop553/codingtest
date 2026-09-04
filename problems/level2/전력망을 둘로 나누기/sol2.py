'''
이건 Claude의 코드
내가 짠 sol1의 코드가 짧긴 했지만
A와 연결된 트리구조를 발견할 때까지 오랜 시간이 걸릴 수 있음
예를 들어, A가 {1, 2}이고 간선이
[[3, 4], [4, 5], [5, 6], [6, 2]]라면
n(n-1)/2, O(E^2) 번 돌게 된다.
이걸 각 Edge(n개)를 빼면서 진행하니까
O(N^3)이 되어 긴 시간이 걸리는데,

원래 인접 리스트를 탐색하는 방법은 Queue를 이용하는 것이다.

'''


from collections import deque

def solution(n, wires):
    ans = n
    for i in range(len(wires)):
        adj = [[] for _ in range(n + 1)]
        for j, (a, b) in enumerate(wires):
            if j == i:
                continue
            adj[a].append(b)
            adj[b].append(a)

        visited = {1}
        q = deque([1])
        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        ans = min(ans, abs(n - 2 * len(visited)))
    return ans