"""
Greedy하게 각각의 노드의 최댓값이 작아지는 방향으로 하면 어떨까?
즉 max(v1, v2)가 최소가 되는 edge를 찾자는 거지
argmin max (v1, v2)
그게 결국 최소가 될까?
증명할 수 있나??

근데 이거 테스트하는 것도 너무 어려운게
자료구조를 어떻게 가져가야 할지도 몰겠음;;
몇 번째 edge라고 할지도 모르겠고
그걸 끊으면 몇대 몇으로 나뉘는지도 알기가 너무 어려움

해당 트리를 돌면서 최댓값이 최소가 되게 분할해주는 함수
"""
n = 3
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
parent = [-1 for _ in range(len(num))]
cum = [-1 for _ in range(len(num))]
delta = [float('inf') for _ in range(len(num))]
top = [-1 for _ in range(len(num))]
for i in range(len(links)):
    left, right = links[i]
    if left != -1: parent[left] = i
    if right!= -1: parent[right] = i

def total(node, root):
    left, right = links[node]
    if left == -1 and right == -1:
        cum[node] = num[node]
    elif right == -1:
        cum[node] = total(left, root) + num[node]
    elif left == -1:
        cum[node] = total(right, root) + num[node]
    else:
        cum[node] = total(left, root) + total(right, root) + num[node]
    top[node] = root
    return cum[node]
root = parent.index(-1)
roots = [root]
total(root, root)
while len(roots) < n:

    root = max(roots, key=lambda i: cum[i])
    total(root, root)
    child = [i for i in range(len(num)) if top[i] == root]
    delta = [max(cum[node], cum[top[node]]-cum[node]) for node in child]
    cut = child[min(range(len(child)), key=lambda i: delta[i])]

    p = parent[cut]
    left, right = links[p]
    if left == cut:
        links[p][0] = -1
    else:
        links[p][1] = -1
    cum[root] = cum[root] - cum[cut]
    parent[cut] = -1
    roots.append(cut)


print(roots)
print(parent)
print(links)
print(cum)
print(max(cum[root] for root in roots))