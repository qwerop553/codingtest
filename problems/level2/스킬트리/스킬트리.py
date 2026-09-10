skill = "CBD"; skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
def solution(skill, skill_trees):
    ans = 0
    for tree in skill_trees:
        j = 0
        for ch in tree:
            if ch in skill:
                if ch != skill[j]:
                    break
                j += 1
                    
            if ch == tree[-1]:
                ans +=1 
    return ans
print(ans)