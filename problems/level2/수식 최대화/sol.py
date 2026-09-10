from functools import reduce
from itertools import permutations
import re
import operator
FUNCS = {"+": operator.add,
         "-": operator.sub,
         "*": operator.mul}

def evaluate(expr, priority):
    if not priority:
        return int(expr)

    *rest, last = priority
    return reduce(FUNCS[last], (evaluate(e, rest) for e in expr.split(last)))

def solution(expr):
    ops = set(re.findall(r"[+\-*]", expr))
    return max(evaluate(expr, p) for p in permutations(ops))

print(solution("20+34*12-32"))