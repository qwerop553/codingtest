
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"


def solution(s):
    k = s[2:-2]
    k = k.split("},{")
    t = list(map(lambda i:map(int, i.split(",")) , k))
    return t

solution(s)
