"""
너무 느려서 실패
"""

def solution(enroll, referral, seller, amount):


    nodes = {'-': [0, None]}
    for psn, ref in zip(enroll, referral):
        nodes[psn] = [0, ref]

    for sell, amt in zip(seller, amount):
        money = amt * 100
        child = nodes[sell]

        child[0] += money
        money = money // 10
        parent = nodes[child[1]]
        while parent:
            child[0] -= money
            parent[0] += money
            money = money // 10
            if money == 0: break
            child = parent
            parent = nodes[child[1]] if child[1] else None

    ans = []
    for psn in enroll:
        ans.append(nodes[psn][0])

    return ans

        
    
