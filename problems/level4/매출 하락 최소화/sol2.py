def solution(sales, links):

    N = len(sales)
    adj = [[] for _ in range(N+1)]
    for a, b in links:
        adj[a].append(b)

    searched = [False for _ in range(N+1)]
    order = []
    candi = [1]
    while candi:
        cur = candi.pop()

        if searched[cur]: # 리프들을 이미 추가했던 노드
            order.append(cur)
            continue

        if not adj[cur]: # 리프 노드
            order.append(cur)
            continue

        candi.append(cur) # 리프가 아니면서 추가하지 않은 노드
        candi.extend(adj[cur])
        searched[cur] = True 


    sales = [0] + sales
    dp1 = [0 for _ in range(N+1)]
    dp0 = [0 for _ in range(N+1)]
    for cur in order:
        if not adj[cur]:
            dp1[cur] = sales[cur]
            dp0[cur] = 0
            continue

        dp1[cur] = sales[cur] + sum(min(dp1[leaf], dp0[leaf]) for leaf in adj[cur])
        dp0[cur] = sum(min(dp1[leaf], dp0[leaf]) for leaf in adj[cur]) if min(dp1[leaf]-dp0[leaf] for leaf in adj[cur]) <0 else min(dp1[leaf]-dp0[leaf] for leaf in adj[cur]) + sum(dp0[leaf] for leaf in adj[cur])


    return min(dp1[1], dp0[1])