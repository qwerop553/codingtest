a = [10, 90]; b = [10, 500]; g=[[100], [70, 70, 0]]; s=[[100], [0, 0, 500]];
w=[[7], [100, 100, 2]]; t=[[10], [4, 8, 1]]; 

i=0; a=a[i];b=b[i];g=g[i];s=s[i];w=w[i];t=t[i];

# Brute Force

# Parametric Search, Deterministic problem으로 고다고.

def possible_time(time, a, b, g, s, w, t):

    total_gold = 0
    total_silver = 0
    total_combine = 0

    for i in range(len(g)):
        total_gold += min(g[i], time // (2 * t[i]) * w[i] + time // t[i] % 2 * w[i])
        total_silver += min(s[i], time // (2 * t[i]) * w[i] + time // t[i] % 2 * w[i])
        total_combine += min(g[i] + s[i], time // (2 * t[i]) * w[i] + time // t[i] % 2 * w[i])
        

    return total_gold >= a and total_silver >= b and total_combine >= a + b

def solution(a, b, g, s, w, t):
    left = 0
    right = 10**15
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if possible_time(mid, a, b, g, s, w, t):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer