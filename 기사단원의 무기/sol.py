number = [5, 10]
limit = [3, 3]
power = [2, 2]
result = [10, 21]

i = 0
number = number[i]; limit = limit[i]; power = power[i]; result = result[i];


def divisors(n):
    count = 0
    for i in range(1, n+1):
        count = count + 1 if n % i == 0 else count
    return count

[divisors(n) for n in range(1,)]