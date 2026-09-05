n = 5
from itertools import chain
def solution(n):
    cur = 1
    cur_level = 0
    levels = [[] for _ in range(n)]
    for i, e in enumerate(range(n, 0, -3)):
        for _ in range(e-1):
            levels[cur_level] = levels[cur_level][:i] + [cur] +levels[cur_level][i:] + levels[cur_level][len(levels[cur_level])//2:]
            cur += 1
            cur_level += 1
        levels[cur_level] = levels[cur_level][:i] + [k for k in range(cur, cur + e - 1)] + levels[cur_level][i:]
        cur += e - 1
        j = len(levels[cur_level])
        for _ in range(e-1):
            levels[cur_level] = levels[cur_level][:j-i] + [cur] + levels[cur_level][j-i:]
            cur += 1
            cur_level -= 1
        cur_level += 2

    return list(chain.from_iterable(levels))

print(solution(5))