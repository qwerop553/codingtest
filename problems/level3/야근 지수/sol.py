import heapq
def solution(n, works):
    if sum(works) <= n: return 0
    heap = [-work for work in works]
    heapq.heapify(heap)
    for _ in range(n):
        heapq.heapreplace(heap, heap[0]+1)
    return sum(w*w for w in heap)
    



    
    
