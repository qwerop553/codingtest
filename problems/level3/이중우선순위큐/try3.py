import heapq
min_q, max_q = [], []
size = 0
alive = []
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
for ops in operations:
    cmd, num = ops.split()

    if cmd == "I":
        heapq.heappush(min_q, (int(num), len(alive)))
        heapq.heappush(max_q, (-int(num), len(alive)))
        alive.append(True)
        size += 1
    
    elif size > 0:
        q = max_q if num == "1" else min_q
        while q and not alive[q[0][1]]:
            heapq.heappop(q)
        _, idx = heapq.heappop(q)
        alive[idx] = False
        size -= 1

if size == 0:
    print([0, 0])
else:
    print([-max_q[0][0], min_q[0][0]])

import heapq
def solution(operations):
    min_q, max_q = [], []
    size = 0
    alive = []

    for ops in operations:
        cmd, num = ops.split()

        if cmd == "I":
            heapq.heappush(min_q, (int(num), len(alive)))
            heapq.heappush(max_q, (-int(num), len(alive)))
            alive.append(True)
            size += 1
        
        elif size > 0:
            q = max_q if num == "1" else min_q
            while q and not alive[q[0][1]]:
                heapq.heappop(q)
            _, idx = heapq.heappop(q)
            alive[idx] = False
            size -= 1

    if size == 0:
        return [0, 0]
    else:
        while min_q and not alive[min_q[0][1]]:
            heapq.heappop(min_q)
        while max_q and not alive[max_q[0][1]]:
                    heapq.heappop(max_q)
        return [-max_q[0][0], min_q[0][0]]

        
    
 
        
        
