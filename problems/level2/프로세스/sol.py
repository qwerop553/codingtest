priorities = [1, 1, 9, 1, 1, 1] 
location = 0


from collections import Counter, deque
importances = list(sorted(dict(Counter(priorities)).items(), reverse=True))

max_priority, left = importances[0][0], importances[0][1]

priorities = zip(priorities, [i for i in range(len(priorities))])

count = 0
q = deque(priorities)
while q:
    cur = q.popleft()
    if cur[0] == max_priority:
        count += 1
        left -= 1
        if left == 0:
            importances.pop(0)
            max_priority, left = importances[0][0], importances[0][1]
        if cur[1] == location:
            break
    else:
        q.append(cur)

print(count)
    


from collections import Counter, deque
def solution(priorities, location):
    importances = list(sorted(dict(Counter(priorities)).items(), reverse=True))

    max_priority, left = importances[0][0], importances[0][1]

    priorities = zip(priorities, [i for i in range(len(priorities))])

    count = 0
    q = deque(priorities)
    while q:
        cur = q.popleft()
        if cur[0] == max_priority:
            count += 1
            left -= 1
            if cur[1] == location:
                break
            if left == 0:
                importances.pop(0)
                max_priority, left = importances[0][0], importances[0][1]
           
        else:
            q.append(cur)

    return count