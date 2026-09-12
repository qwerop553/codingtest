"""
DP로 풀어보자.

n번째에 k를 만드는 방법은 몇 가지가 있는가?
이 문제를 풀기 위해선 n-1번째에 만들 수 있는 
모든 s에 대하여 s를 만드는 모든 방법만 알면 된다.

왜 Counter를 쓰는가?
counter랑 defaultdict는 같다.
없는 값에 대해서 0을 돌려주는. 그래서 사실 defaultdict 쓰는 거랑 같아보임
"""

from collections import Counter

def solution(numbers, target):
    cur = Counter([0])
    for i in range(0, len(numbers)):
        nxt = Counter()
        for num, cnt in cur.items():
            nxt[num + numbers[i]] += cnt
            nxt[num - numbers[i]] += cnt
        cur = nxt

    return cur[target]

numbers = [1, 1, 1, 1, 1]
solution(numbers)
