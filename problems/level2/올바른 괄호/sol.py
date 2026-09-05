def solution(s):
    idx = -1
    for ss in s:

        if ss == '(':
            idx += 1
            continue

        if idx == -1:
            return False

        idx -= 1

    return idx == -1

