import math
def solution(progresses, speeds):
    ans = []
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    cnt, d  = 0, days[0] 
    for t in days:
        if t <= d:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            d = t
    ans.append(cnt)
    return ans
