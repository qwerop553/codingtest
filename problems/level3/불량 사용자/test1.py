user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

N, M = len(banned_id), len(user_id)

def match(banned_id, user_id):
    n, m = len(banned_id), len(user_id)
    if (n != m): return False 
    for i in range(n):
        if banned_id[i] == '*': continue
        if banned_id[i] != user_id[i]: return False
    return True 

matches = []
for ban_id in banned_id:
    matches.append([i for i, id in enumerate(user_id) if match(ban_id, id)])
print(matches)
            
cnt = 0
result = set()
from itertools import product
for combo in product(*matches):
    if len(combo) == len(set(combo)):
        result.add(frozenset(combo))

print(len(result))



