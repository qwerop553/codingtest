operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]


from collections import deque
ss = [(a, int(b)) for operation in operations for a, b in [operation.split()]]
print(ss)

q = deque([])
for op, num in ss:
    if op == 'I':
        q.append(num)
        q = deque(sorted(q))
        continue
    if q:
        if op == 'D' and num==1:
            q.pop()
        else:
            q.popleft()

if len(q) >= 2:
    ans = [q.pop(), q.popleft()]
elif len(q) == 1:
    ans = [q[0], q[0]]
else:
    ans = [0, 0]

print(ans)

from collections import deque
def solution(operations):
    ss = [(a, int(b)) for operation in operations for a, b in [operation.split()]]

    q = deque([])
    for op, num in ss:
        if op == 'I':
            q.append(num)
            q = deque(sorted(q))
            continue
        if q:
            if op == 'D' and num==1:
                q.pop()
            else:
                q.popleft()

    if len(q) >= 2:
        ans = [q.pop(), q.popleft()]
    elif len(q) == 1:
        ans = [q[0], q[0]]
    else:
        ans = [0, 0]

    return ans