def alphabet(n):
    if n <= 9: return(str(n))
    match n:
        case 10: return ('A')
        case 11: return ('B')
        case 12: return ('C')
        case 13: return ('D')
        case 14: return ('E')
        case 15: return ('F')
        
def to_digit(n, digit) -> str:

    if n == 0: return '0'

    ans = ''
    q, r = divmod(n, digit)
    while (q, r) != (0, 0):
        ans += alphabet(r)
        q, r = divmod(q, digit)
        
    ans = ans[::-1]

    return ans

from itertools import chain
import math
def solution(n, t, m, p):
    est = pow(n, math.ceil(math.log(m * t, n)))
    ans = list(chain.from_iterable(to_digit(i, n) for i in range(est)))

    ret = ''
    for i in range(p-1, m*t, m):
        ret += ans[i]

    return ret

