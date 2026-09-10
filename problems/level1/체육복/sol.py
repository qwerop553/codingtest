n = 5; lost = [2, 4]; reserve = [1, 3, 5];

def solution(n):
    ans = 0; j = 0 
    for i in range(len(lost)):
        for k in range(j, len(reserve)):
            if (lost[i] == reserve[k] - 1 or lost[i] == reserve[k] + 1):
                j = k + 1
                ans += 1
                break

    return ans + len(reserve)
    