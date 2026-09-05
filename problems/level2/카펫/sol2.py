from collections import deque, Counter

def solution(priorities, location):
    cnt = Counter(priorities)
    cur = max(cnt)
    q = deque(enumerate(priorities))

    count = 0
    while True:
        idx, pri = q.popleft()

        if pri < cur:
            q.append((idx, pri))
            continue

        count += 1
        if idx == location:
            return count

        cnt[pri] -= 1
        if cnt[pri] == 0:
            del cnt[pri]
            cur = max(cnt) if cnt else 0