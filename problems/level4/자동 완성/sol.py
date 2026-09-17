def solution(words):
    words.sort()
    ans = 0
    test = [max(cnt(words[i], words[i+1]), cnt(words[i], words[i-1])) for i in range(1, len(words)-1)]
    for t in test:
        ans += t
    ans += cnt(words[0], words[1])
    ans += cnt(words[-1], words[-2])
    
    return ans



def cnt(cur, nxt):
    m = min(len(cur), len(nxt))
    i = 0
    while i < m and cur[i] == nxt[i]:
        i += 1
    return i+1 if i+1 < len(cur) else len(cur) 
