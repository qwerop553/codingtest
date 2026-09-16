def solution(k, num, links):
    parent = [-1 for _ in range(len(num))]
    cum = [-1 for _ in range(len(num))]
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

    while len(roots) < k:
        root = max(roots, key=lambda i: cum[i])
        
        child = [i for i in range(len(num)) if top[i] == root]
        delta = [max(cum[node], cum[top[node]]-cum[node]) for node in child]
        cut = child[min(range(len(child)), key=lambda i: delta[i])]

        p = parent[cut]
        left, right = links[p]
        if left == cut:
            links[p][0] = -1
        elif right == cut:
            links[p][1] = -1
        parent[cut] = -1
        roots.append(cut)
        total(root, root)
        total(cut, cut)

    return max(cum[root] for root in roots)

print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))