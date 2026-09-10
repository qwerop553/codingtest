arr = [2,6,8,14]

import math
from functools import reduce
# 약수를 만들어 내는 함수
def gcd(a, b):
    a, b = min(a, b), max(a, b)
    for i in range(a, 0, -1):
        if a%i == b%i == 0:
            return i
    return 1

def lcd(a, b):
    return a * b // gcd(a, b)


print(reduce(lcd, arr))




