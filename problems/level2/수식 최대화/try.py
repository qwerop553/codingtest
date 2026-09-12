"""
중위 연산자는
해당 값을 기준으로 좌와 우로 나누면 된다.
대신 이게 연산순위가 낮은 거 부터.

reduce란 함수는 reduce(적용할 함수, 적용될 값들을 담고 있는 iterable, [Optional|초기값])
그리고 operators. reduce에 (+, range(..)) 로 날 것으로 쓸 순 없으니까..

re 패키지. 정규식(regular expression) 패키지인데 그냥 문자열 처리 패키지라고 보면 되겠다.
그리고 itertools의 permutations은 그냥 그 iterable을 넘기면 nPn permutation을 지급한다.
"""

expression = "100-200*300-500+20"	

import re
import operator
from functools import reduce
from itertools import permutations

def solution(expression):
    OPERATIONS = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul}

    def r_fun(exp, ops):
        if not ops:
            return int(exp)
        *rest, last = ops
        return reduce(OPERATIONS[last], (r_fun(e, rest) for e in exp.split(last)))


    ops = set(re.findall(r'[+\-*]', expression))
    return max(abs(r_fun(expression, p)) for p in permutations(ops)) 






