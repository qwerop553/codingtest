def solution(edges):
    n = max(map(max, edges))
    indeg = [0] * (n + 1)
    outdeg = [0] * (n + 1)
    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1

    generated = line = eight = 0
    for v in range(1, n + 1):
        if indeg[v] == 0 and outdeg[v] >= 2:
            generated = v
        elif outdeg[v] == 0 and indeg[v] >= 1:
            line += 1
        elif indeg[v] >= 2 and outdeg[v] >= 2:
            eight += 1

    donut = outdeg[generated] - line - eight
    return [generated, donut, line, eight]