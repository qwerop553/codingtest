a = 2; b = 1; n = 20;

result = 0
while n >= a:
    q, r = divmod(n, a)
    result += q
    n = q * b + r

print(result)