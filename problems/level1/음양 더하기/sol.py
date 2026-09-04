def solution(absolutes, signs):
    ans = 0
    for n, s in zip(absolutes, signs):
        ans += n if s else -n
    return ans

print(solution([4, 7, 12], [True, False, True]))
