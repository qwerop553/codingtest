def solution(cookie):
    n = len(cookie)
    total = sum(cookie)
    bounds = []
    prefix = 0
    for m in range(n-1):
        prefix += cookie[m]
        bounds.append((min(prefix, total-prefix), m))
    bounds.sort(reverse=True)

    ans = 0
    for bound, m in bounds:
        if bound <= ans:
            break # 싸그리 날려버림
        l, r = m, m + 1
        left, right = cookie[l], cookie[r]
        while True:
            if left == right:
                ans = max(ans, left)
            if left < right:
                l -= 1
                if l < 0: break
                left += cookie[l]
            else:
                r += 1
                if r == n: break
                right += cookie[r]
    return ans 