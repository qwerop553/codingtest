"""
GREEDY 한 경우에 반례 있음..
3-2-1-3을 세 그룹으로 나누는 경우
3-2|1-3 으로 나누는 게 처음에 가장 좋은 선택이지만
best case는 3|2-1|3임

그래서 Parametric Search를 해보자.
"""
k = 3
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
def solution(k, num, links):
    parent = [-1 for _ in range(len(num))]

    for i in range(len(links)):
        left, right = links[i]
        if left != -1: parent[left] = i
        if right!= -1: parent[right] = i

    root = 0
    while parent[root] != -1:
        root = parent[root]

    order = []
    stack = [root]
    while stack:
        v = stack.pop()
        order.append(v)
        for c in links[v]:
            if c != -1:
                stack.append(c)
    order.reverse()
    n = len(num)

    def count_groups(L):
        up = [0] * n   # up[v]: v 서브트리에서 v와 같은 그룹으로 위에 올려보내는 인원
        cnt = 0        # 잘라낸 횟수
        for v in order:
            left, right = links[v]
            lv = up[left] if left != -1 else 0
            rv = up[right] if right != -1 else 0
            if lv + rv + num[v] <= L: up[v] = lv + rv + num[v]
            else:
                vv = lv if lv <= rv else rv
                if vv + num[v] <= L: 
                    up[v] = vv + num[v]
                    cnt += 1
                else:
                    up[v] = num[v]
                    cnt += 2
        return cnt + 1

    L, R = max(num), sum(num)
    while True:
        if R-L <= 1: 
            return L if count_groups(L) <= k else R
        if count_groups((L+R)//2) > k:
            L = (L+R)//2
        else:
            R = (L+R)//2
        
