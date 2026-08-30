number = [5, 10]
limit = [3, 3]
power = [2, 2]
result = [10, 21]

i = 1
number = number[i]; limit = limit[i]; power = power[i]; result = result[i];


def divisors(n, limit, power):
    count = 0
    for i in range(1, n+1):
        count = count + 1 if n % i == 0 else count
        if count > limit: break
    return count if count <= limit else power

print(sum([divisors(n, limit, power) for n in range(1, number+1)]))

# 시간 에러 발생(시간 내 풀이가 다 안된다)
# 그래도 에러 발생