numbers = [1, 1, 1, 1, 1]; target = 3;

N = len(numbers)
ans = 0



def solution(numbers, target):
    N = len(numbers)
    ans = 0

    def dfs(i, total):
        nonlocal ans
        if i== N:
            if total == target:
                ans += 1
            return

        dfs(i+1, total+numbers[i])
        dfs(i+1, total-numbers[i])

    dfs(0, 0)
    return ans
    
