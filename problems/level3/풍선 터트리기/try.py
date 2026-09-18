def solution(a):
    n = len(a)
    left = [0] * n
    right = [0] * n
    left[0] = a[0]
    right[-1] = a[-1]
    for i in range(1, len(a)):
        left[i] = min(left[i-1], a[i])
    for i in range(len(a)-2, -1, -1):
        right[i] = min(right[i+1], a[i])
    ans = 0
    for i in range(len(a)):
        if i == 0 or i == len(a) - 1: 
            ans += 1 
            continue
        if left[i-1] < a[i] and right[i+1] < a[i]:
            continue
        ans += 1
    return ans


# 이렇게 생각할 수 있음..
# 시발
# 아니 그니까 
# 왼쪽에서 나보다 작은 녀석이 있으면서 오른쪽에서도 나보다 작은 녀석이 있으면 최후의 풍선이 아니다.
# 대우명제로
# 최후의 풍선이면 왼쪽에 나보다 작은 녀석이 없거나, 오른쪽에 나보다 작은 녀석이 없다.
# 즉 왼쪽에서 가면서 최솟값인 녀석을 만나면, 그 녀석은 최후의 풍선이다.
# 오른쪽도 마찬가지
# 대신 그렇게 긁는데, 왼쪽에서도 최소이면서 오른쪽에서 최소인 녀석은
# 전체에서 최소인 풍선 뿐이다.
# 믿 힌 ㄷ ㄷ
def solution(a):
    def records(xs):          # 최솟값을 갱신하는 원소 개수
        m = float('inf')
        c = 0
        for x in xs:
            if x < m:
                m, c = x, c + 1
        return c
    return records(a) + records(reversed(a)) - 1