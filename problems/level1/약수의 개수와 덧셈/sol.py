import math
def isEvenDivisors(n: int):
    n_divisors = 0
    for i in range(1, math.isqrt(n)+1):
        if n % i == 0:
            n_divisors += 2
            if n // i == i:
                n_divisors -= 1
    return True if n_divisors % 2 ==0 else False


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer += i if isEvenDivisors(i) else -i
    return answer

print(solution(13, 17))