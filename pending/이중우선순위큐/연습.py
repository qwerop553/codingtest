import heapq

def solution(operations):

    max_q, min_q = [], []
    alive = []; size = 0

    def clean(q):
        while q and not alive(q[0][1]):
            pass

    for op in operations:
        cmd, arg = op.split()

        if cmd == "I":
            value, idx = int(arg), len(alive)
            alive.append(True)
            heapq.heappush(max_q, (-value, idx))
            heapq.heappush(min_q, (value, idx))
            size += 1 

        elif size:
            q = max_q if arg == "1" else min_q
            clean(q)
            alive[q[0][1]] = False
            size -= 1

    if size == 0:
        return [-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0]]

