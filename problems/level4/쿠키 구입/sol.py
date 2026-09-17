def solution(cookie):
    ans = 0
    for k in range(len(cookie)-1):
        i, j = k, k + 1
        first, second = cookie[i], cookie[j]
        while True:
            if first == second: ans = max(ans, first)
            if first < second:
                i -= 1
                if i == -1: break
                first += cookie[i]
            else:
                j += 1
                if j == len(cookie): break
                second += cookie[j]
                
    return ans


