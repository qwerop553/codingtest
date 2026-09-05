from collections import Counter, deque 
priorities = [2, 1, 3, 2]; location =2;
counter = Counter(priorities)
count = 0

max_importance = max(counter)
q = deque(enumerate(priorities))
while q:
    p = q.popleft()
    p_loc, p_imp = p[0], p[1]
    if p_imp == max_importance:
        count += 1
        if p_loc == location: break
        counter[max_importance] -= 1
        if counter[max_importance] == 0: 
            del counter[max_importance]
            max_importance = max(counter)

    else:
        q.append(p)

print(count)

from collections import Counter, deque 
def solution(priorities, location):
    counter = Counter(priorities)
    count = 0

    max_importance = max(counter)
    q = deque(enumerate(priorities))
    while q:
        p = q.popleft()
        p_loc, p_imp = p[0], p[1]
        if p_imp == max_importance:
            count += 1
            if p_loc == location: break
            counter[max_importance] -= 1
            if counter[max_importance] == 0: 
                del counter[max_importance]
                max_importance = max(counter)

        else:
            q.append(p)

    return count
