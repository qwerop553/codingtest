clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    hs = {}
    for cloth, tp in clothes:
        hs[tp] = hs.get(tp, 0) + 1

    ans = 1
    for _, b in hs.items():
        ans *= b+1

    return ans-1

    
