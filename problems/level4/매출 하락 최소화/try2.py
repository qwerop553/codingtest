sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

N = len(sales)
adj = [[] for _ in range(N+1)]
for a, b in links:
    adj[a].append(b)

print("adjacent list: ", adj)

searched = [False for  _ in range(N+1)]
order = []
candi = [1]
while candi:
    cur = candi.pop()

    if searched[cur]: # 리프들을 모두 추가했던 노드
        order.append(cur)
        continue

    if not adj[cur]: # 리프 노드
        order.append(cur)
        continue

    candi.append(cur) # 리프가 아니고 추가한 적 없던 노드
    candi.extend(adj[cur])
    searched[cur] = True

print(order)
sales = [0] + sales
INF = float('inf') 
dp1 = [0 for _ in range(N+1)]
dp0 = [0 for _ in range(N+1)]
for cur in order:
    if not adj[cur]:
        dp1[cur] = sales[cur]
        dp0[cur] = 0
        continue

    dp1[cur] = sales[cur] + sum(dp0[leaf] for leaf in adj[cur])
    dp0[cur] = min(dp1[leaf]-dp0[leaf] for leaf in adj[cur]) + sum(dp0[leaf] for leaf in adj[cur])

print("dp1: ", dp1)
print("dp0: ", dp0)

print("the answer is: ", min(dp1[1], dp0[1]))