from collections import deque
progresses = [93, 30, 55]
speeds = [1, 30, 5]

q = deque(progresses)
out = 0
ans = []
while q:
  
    if q[0] < 100:
        for i in range(len(q)):
            q[i] += speeds[i]

    
    while q and q[0] >= 100:
        q.popleft()
        out += 1

    if out > 0:
        ans.append(out)
        out = 0

            

print(ans)

from collections import deque
def solution():
    q = deque(progresses)
    s = deque(progresses)
    out = 0
    ans = []
    while q:
        if q[0] < 100:
            for i in range(len(q)):
                q[i] += speeds[i]

        while q and q[0] >= 100:
            q.popleft()
            s.popleft()
            out += 1

        if out > 0:
            ans.append(out)
            out = 0
    return ans 
