"""
답은 맞는데 
너무 느리다
"""

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

import heapq
def solution(sales, links):
    N = len(sales)
    adj = [[i] for i in range(N+1)]
    for boss, empl in links:
        adj[boss].append(empl)

    teams = [team for team in adj if len(team) > 1]
    M = len(teams)

    q = [(0, 0, [])] # 현재 매출, # 몇 번째 팀까지 포함했는지, # 누굴 포함했는지
    while q:
        sale, cnt, plist = heapq.heappop(q)
        if cnt == M:
            return sale
        
        for p in teams[cnt]:
            if p in plist:
                heapq.heappush(q, (sale, cnt+1, plist))
            else:
                heapq.heappush(q, (sale+sales[p-1], cnt+1, plist + [p]))
    return -1