s = ["banana", "abracadabra", "aaabbaccccabba"]

i = 2
s = s[i]

ret = 0
is_new = True
i = 0
while i < len(s):
    if is_new:
        ch = s[i]
        i = i + 1
        ch_count = 1
        other_count = 0
        is_new = False
    else:
        if s[i] == ch:
            ch_count += 1
        else:
            other_count += 1
        i += 1
        if ch_count == other_count:
            ret += 1
            is_new = True
if not is_new:
    ret += 1

print(ret)

def solution(s):
    answer = 0
    ch_count = 0
    for ch in s:
        if ch_count == 0:
            cs = ch
            other_count = 0
            ch_count += 1
        else:
            if cs == ch:
                ch_count += 1
            else:
                other_count += 1
            if ch_count == other_count:
                answer += 1
                ch_count = 0
    if ch_count != 0:
        answer += 1
    return answer

