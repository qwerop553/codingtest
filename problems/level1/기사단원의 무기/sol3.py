number = [5, 10]
limit = [3, 3]
power = [2, 2]
result = [10, 21]

i = 1
number = number[i]; limit = limit[i]; power = power[i]; result = result[i];



def divisors(n, limit, power):
    ret = {}
    for i in range(2, n+1):
        while n % i == 0:
            ret[i] = ret[i] + 1 if i in ret else 1
            n = n / i
        if n == 1: break

    temp = 1
    for i in ret.values():
        temp *= i + 1
    return temp if temp <= limit else power


def solution(n, limit, power):
    return sum([divisors(n, limit, power) for n in range(1, number+1)])

# 소인수 분해 형식으로 접근해 보았다.
# 그래도 일부 에러 발생 (66.7/100)