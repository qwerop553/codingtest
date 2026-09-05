
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"


def solution(s):
    k = s[2:-2] # 2},{2,1},{2,1,3},{2,1,3,4
    k = k.split("},{") # ["2", "2,1", "2,1,3", "2,1,3,4"]
    t = list(map(lambda i:list(map(int, i.split(","))) , k)) # [[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]
    t.sort(key=lambda i: len(i))
    ans = []
    for nums in t:
        for num in nums:
            if num not in ans:
                ans.append(num)
    return ans

print(solution(s))
