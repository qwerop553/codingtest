DIGITS = "0123456789ABCDEF"

def to_base(num, base):
    if num == 0: 
        return '0'
    out = []
    while num:
        num, r = divmod(num, base)
        out.append(DIGITS[r])

    return "".join(reversed(out))


def solution(n, t, m, p):
    need = m * t
    parts, length, i = [], 0, 0
    while length < need:
        s = to_base(i, n)
        parts.append(s)
        length += len(s)
        i += 1
    return "".join(parts)[p-1: need : m]
