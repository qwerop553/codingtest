number = [5, 10]
limit = [3, 3]
power = [2, 2]
result = [10, 21]

i = 1
number = number[i]; limit = limit[i]; power = power[i]; result = result[i];

import math

def divisors(n, limit, power):
    count = 0
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            if n / i == i:
                count += 1
                continue
            count += 2

    return count if count <= limit else power


def solution(n, limit, power):
    return sum([divisors(n, limit, power) for n in range(1, number+1)])

print(solution(number, limit, power))