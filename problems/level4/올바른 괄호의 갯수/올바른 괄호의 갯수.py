n = 2;
from collections import Counter

nxt = Counter([0])
for i in range(2*n):
    cur = Counter()
    for left, cnt in nxt.items():
        right = i - left
        if left > right:
            cur[left+1] += cnt
            cur[left] += cnt
        elif left == right:
            cur[left+1] += cnt
        nxt = cur

print(nxt)

from collections import Counter
def solution(n):
    nxt = Counter([0])
    for i in range(2*n):
        cur = Counter()
        for left, cnt in nxt.items():
            right = i - left
            if left > right:
                cur[left+1] += cnt
                cur[left] += cnt
            elif left == right:
                cur[left+1] += cnt
        nxt = cur
    return nxt[n]

