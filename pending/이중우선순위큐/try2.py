import heapq

def solution(operations):
    min_q, max_q = [], []
    alive = []
    size = 0

    def clean(q):
        while q and not alive[q[0][1]]:
            heapq.heappop(q)

    for op in operations:
        cmd, arg = op.split()

        if cmd == "I":
            value, idx = int(arg), len(alive)
            alive.append(True)
            heapq.heappush(min_q, (value, idx))
            heapq.heappush(max_q, (-value, idx))
            size += 1

        elif size:
            q = max_q if arg == '1' else min_q
            clean(q)
            alive[heapq.heappop(q)[1]] = False
            size -= 1

    if not size:
        return [0, 0]
    clean(min_q); clean(max_q)
    return [-max_q[0][0], min_q[0][0]]