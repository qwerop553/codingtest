number = [-2, 3, 0, 2, -5]


import itertools



result = 0
for a, b, c in list(itertools.combinations(number, 3)):
    if a+b+c==0:
        result += 1

print(result)