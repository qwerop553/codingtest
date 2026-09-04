brown = 10; yellow = 2;

import math
def solution(brown, yellow):
    for n in range(1, math.floor(math.sqrt(yellow))+1):
        q, r = divmod(yellow, n)
        if r == 0:
            width, height = max(n, q) + 2, min(n, q) + 2
            if 2 * (width + height) - 4 == brown:
                return (width, height)
    raise Exception()